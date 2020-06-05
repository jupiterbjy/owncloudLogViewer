from itertools import takewhile, repeat
from os import path
from collections import Sequence
from functools import lru_cache
import re
import json
import datetime


class LazyLineLoader(Sequence):
    """
    Provides Sequence methods to large line-separated files.
    Focus on memory, by sacrificing performance.

    Will use chunk approach to this.
    """

    def __init__(self, file_dir, ignore_blank_lines=True):
        self.f_dir = file_dir
        self.f_name = path.split(file_dir)[1]
        self.ign_blank = ignore_blank_lines

    # lru_cahce(user_function) was added, but don't get what it's for.
    # I doubt if I can cache __getitem__ with functools.cached_property.
    # @lru_cache(maxsize=512, typed=True)
    # caching cause new instance using old cached data.
    def __getitem__(self, idx: int) -> str:
        for current, line in enumerate(lineReturn_Gen(self.f_dir, self.ign_blank)):
            if current == idx:
                return line

    def __len__(self):
        if self.ign_blank:
            return fileLineCounter_blankIgnore(self.f_dir)
        return fileLineCounter(self.f_dir)

    def readLine(self, index):
        if self.ign_blank:
            return


# 0.3456418000000099
def fileLineCounter(file_name):
    with open(file_name, "rb") as f:
        buf_gen = takewhile(lambda x: x, (f.read(1024 * 1024) for _ in repeat(None)))
        return sum(buf.count(b"\n") for buf in buf_gen)


# 1.4647625000000062, At least memory-efficient, I believe..
def fileLineCounter_blankIgnore(file_name):
    count = 0
    with open(file_name, "rt") as f:
        for line in f:
            if line == "\n":
                continue
            count += 1
        return count


# --------------------------------


class LazyJsonLoader(Sequence):
    def __init__(self, file_dir):
        self.f_dir = file_dir
        self.f_name = path.split(file_dir)[1]
        self.LazyLoader = LazyLineLoader(file_dir)
        self.is_owncloud = False

    def __getitem__(self, idx) -> json:
        source = self.LazyLoader[idx]
        json_src = jsonParser(source)

        if not isinstance(json_src["message"], dict):
            result = owncloudJsonParser(json_src["message"])
            json_src["message"] = result

        return json_src

    def __len__(self):
        return len(self.LazyLoader)


def numericToAlphabet(total_, line_index):
    def digit(num, base=10):
        if num == 0:
            return 0
        return digit(num // base) + 1

    out = "0" * (digit(total_) - digit(line_index))

    if line_index == 0:
        return out
    return out + str(line_index)


def lineReturn_Gen(file_name, ignore_blank=True):
    with open(file_name, "rt") as file:
        if ignore_blank:
            for line in file:
                if line == "\n":  # sometimes owncloud logs has blank lines.
                    continue
                yield line
        else:  # Not so compact, but will have performance benefit.
            for line in file:
                yield line


def jsonParser(text) -> dict:
    try:
        json_output = json.loads(text)
    except json.decoder.JSONDecodeError:
        raise Warning("Failed converting to JSON. Got this:", text)
    else:
        return json_output


def owncloudJsonParser(message: str) -> dict:
    result = owncloudErrorExtract(message)

    try:
        json_output = jsonParser(result)
    except Warning:
        return {"Exception": result}

    return json_output


def owncloudErrorExtract(message):
    pattern = r"^([^{]+)"
    if "{" in message:
        return re.sub(pattern, "", message)

    return message


def jsonLine_Gen(file_name):  # deprecated
    for line in lineReturn_Gen(file_name):
        yield jsonParser(line)


def unified_Generator(file_name):
    """
    Json Generator that deals with Compatibility.
    Converts Owncloud Format to Nextcloud format and yield.
    """
    for json_line in jsonLine_Gen(file_name):
        message = json_line["message"]

        if isinstance(message, dict):  # nextcloud dict
            pass
        else:  # owncloud string
            while not isinstance(message, dict):
                message = owncloudJsonParser(message)

            json_line["message"] = message

        yield json_line


def timeConvert(time_string):
    t = time_string.split("+")[0]
    dt_obj = datetime.datetime.strptime(t, "%Y-%m-%d %H:%M:%S")
    return dt_obj


def lineProcess_new(file_name):
    """
    Formats json to fit in nice 8-column item.
    """
    total = fileLineCounter(file_name)

    for idx, json_l in enumerate(unified_Generator(file_name)):
        app_name = json_l["app"]
        time_ = json_l["time"].split("+")[0]
        level = " " + str(json_l["level"])

        form = [
            numericToAlphabet(total, idx),
            time_.replace("T", " "),
            level,
            json_l["remoteAddr"],
            json_l["user"],
            app_name,
            json_l["method"],
            json_l["message"]["Exception"],
        ]

        yield form


# Debugging function
if __name__ == "__main__":

    output = lineProcess_new("./testcase/owncloud.log")

    if not isinstance(output, int):
        for txt in output:
            for i in txt:

                print("*" + i + "*")
