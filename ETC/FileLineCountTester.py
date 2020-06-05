import timeit
from itertools import takewhile, repeat
from functools import partial

FILE = r"Z:\github\owncloudLogViewer\owncloud (2).log"

out = 0


# Reference:
# https://stackoverflow.com/questions/9629179/
# https://stackoverflow.com/questions/845058/


def test_A():  # By glglgl
    global out

    def blocks(files, size=65536):
        while True:
            b = files.read(size)
            if not b:
                break
            yield b

    with open(FILE, "r", encoding="utf-8", errors="ignore") as f:
        out = (sum(bl.count("\n") for bl in blocks(f)))


def test_B():
    global out

    def count_lines(file):
        idx = 0     # pycharm wants this..
        for idx, l in enumerate(file):
            pass

        return idx

    with open(FILE, "r", encoding="utf-8", errors="ignore") as f:
        out = (count_lines(f))


def test_C():
    global out

    def count_lines(filename):  # by Michael Bacon
        bufgen = takewhile(lambda x: x, (f.read(1024 * 1024) for _ in repeat(None)))
        return sum(buf.count(b'\n') for buf in bufgen)

    with open(FILE, "rb") as f:
        out = (count_lines(f))


def test_D():
    global out

    def count_lines(filename):  # By jeffpkamp
        buffer = 2 ** 16
        return sum(x.count('\n') for x in iter(partial(filename.read, buffer), ''))

    with open(FILE, "r") as f:
        out = (count_lines(f))


if __name__ == '__main__':

    tests = [test_A, test_B, test_C, test_D]
    results = []

    for t in tests:
        result = timeit.timeit(t, number=20)
        print(out, result)
        results.append(result)

    idx = results.index(min(results))
    print(tests[idx].__name__, "is fastest.")
