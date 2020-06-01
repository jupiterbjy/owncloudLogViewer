from PySide2.QtCore import QCoreApplication, QEventLoop
from itertools import takewhile, repeat
import re
import json


def fileLineCounter(file_name):
    with open(file_name, 'rb') as f:
        buf_gen = takewhile(lambda x: x, (f.read(1024 * 1024) for _ in repeat(None)))
        return sum(buf.count(b'\n') for buf in buf_gen)


def numericToAlphabet(total, line_index):
    def digit(num, base=10):
        if num == 0:
            return 0
        else:
            return digit(num//base) + 1
    
    out = '0'*(digit(total) - digit(line_index))
    
    if line_index == 0:
        return out
    else:
        return out + str(line_index)
    
    
def openWrapper(loc, mode='rt'):
    try:
        f = open(loc, mode)

    except FileNotFoundError:
        return 0
    else:
        return f


def lineReturn_Gen(file_name):
    with open(file_name, 'rt') as file:
        for line in file:
            yield line


def jsonParser(text):
    try:
        json_output = json.loads(text)
    except json.decoder.JSONDecodeError:
        raise Warning('Failed converting to JSON. Got this:', text)
    else:
        return json_output


def jsonLine_Gen(file_name):
    for line in lineReturn_Gen(file_name):
        if line == '\n':  # sometimes Owncloud logs has blank line spamming.
            continue

        yield jsonParser(line)


def unified_Generator(file_name):
    """
    Json Generator that deals with Compatibility.
    Converts Owncloud Format to Nextcloud format and yield.
    """
    for json_line in jsonLine_Gen(file_name):

        message = json_line['message']

        if isinstance(message, dict):  # nextcloud dict
            pass
        else:  # owncloud string
            result = re.sub(r'(^[^:]*:)([^:]*:)', '', message)

            try:
                json_output = jsonParser(result)
            except Warning:
                json_line['message'] = {'Exception': message}
                pass  # log is simple string, like 'login failed.'
            else:
                json_line['message'] = json_output

        yield json_line


def lineProcess_new(file_name):
    """
    Formats json to fit in nice 8-column item.
    """
    global total
    total = fileLineCounter(file_name)

    for idx, json_l in enumerate(unified_Generator(file_name)):
        form = [numericToAlphabet(total, idx), json_l['time'], json_l['level'], json_l['remoteAddr'], json_l['user'],
                json_l['app'], json_l['method'], json_l['message']['Exception']]

        yield form


def lineProcess(location, limit=-1, blacklist=None):

    if blacklist is None:
        blacklist = ['.*reqId.*', '.*url.*']

    def swap(arr, idx1, idx2):
        arr[idx1], arr[idx2] = arr[idx2], arr[idx1]

    # Won't print when called via UI class
    # -------------------------------------
    file = openWrapper(location)
    if not file:
        print('filenotfound')
        return 0
    # -------------------------------------
    
    with file as f:
        file_end = fileLineCounter(openWrapper(location))
        output_ = []

        # TODO: add generic error handling during line read - ignoring wrong line.

        for line, text in enumerate(f):
            
            # checking this condition on every line doesn't sound great.
            if line == limit:
                break

            # owncloud sometimes generate random newline spams.
            if text == '\n':
                continue

            text_arr = text.split(',"')
            index = numericToAlphabet(file_end, line)
            item = [index]

            for idx, txt_ in enumerate(text_arr):

                # checking if txt contains blacklists
                # ----------------------------------
                remove = False
                
                for bl in blacklist:
                    if re.match(bl, txt_):
                        remove = True
                        
                if remove:
                    continue
                else:
                    txt_ = re.sub('"', '', txt_)
                # ----------------------------------

                if re.match('message', txt_):
                    # Silly way of using regex, but more readable I guess.
                    
                    msg = re.sub('message', '', txt_)
                    # msg = msg.replace(':', '', 1)
                    # msg = msg.replace('\\', '/')
                    # msg = re.sub('/+', '/', msg)
                    
                    item.append(msg)
                    
                else:

                    txt_ = re.sub('}', '', txt_)
                    txt_ = re.sub(':', ',', txt_, 1)
                    txt_ = re.sub('.*,', '', txt_)
                    item.append(str(txt_))
            
            # Post process

            QCoreApplication.processEvents(QEventLoop.ExcludeUserInputEvents)
            print(text, line)
            swap(item, 1, 2)

            # Time format
            # Removing Timezone for now
            # TODO: add Timezone indicator
            source = (item[1].split('+'))[0]
            item[1] = ' '.join(source.split('T'))
            
            if item[3] == '':
                item[3] = '--'
            if item[5] == 'no app in context':
                item[5] = '--'
            
            output_.append(item)

    return output_
    
    
# Debugging function
if __name__ == '__main__':
    
    output = lineProcess('./testcase/owncloud.log', limit=30)
    
    if not isinstance(output, int):
        for txt in output:
            for i in txt:

                print('*' + i + '*')

global total
