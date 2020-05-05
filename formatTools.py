import member_loader


def rgbToHex(r=0, g=0, b=0):
    arr = [r, g, b]
    out = [str(hex(i))[2:].zfill(2) for i in arr]
    return "#" + "".join(out)


def QtColorize(text, color=(0, 0, 0), size=None, weight=None):
    start = '<span style=" '
    font = f"font-size:{size}pt; " if size else ""
    font_weight = f"font-weight:{weight}; " if size else ""
    color = f"color:{rgbToHex(*color)}; "
    end = '" >'
    txt = str(text)
    span_complete = "</span>"

    out = [start, font, font_weight, color, end, txt, span_complete]

    return "".join(out)


def lvlColorizer(source):
    def slicer(start, end, counts):
        steps = (end - start) // (counts - 1)
        for i in range(start, end + 1, steps):
            yield i

    n = int(source)
    lvlArray = [(r, 0, 0) for r in slicer(0, 255, 5)]

    return QtColorize(source, color=lvlArray[n])


def messageFormating(source, color=True):
    """
    Formot Owncloud Error Messages for better readability.
    Due to lack of experience & time on regex, things became messy.
    """

    import re

    source = source.replace(":", "", 1)
    source = source.replace("\\", "/")
    source = re.sub("/+", "/", source)

    matching = re.findall(r"#\d*\s", source)
    output = source[::]

    if color:
        for case in matching:
            output = output.replace(case, QtColorize(case, color=(255, 0, 0)), 1)

        output = output.replace("/n<", "<br/><")

    else:
        output = output.replace("/n#", "<br/>#")

    output = output.replace("#0", "<br/>#0")
    # output = re.sub('#\d*}', '', output)
    output = re.sub(r"(}+(\n)*)+$", "", output)
    output = re.sub(r"{/Exception[\s\S]*/Trace/:/", "<br/> Trace :", output)

    # There should me more Pythonic way, not reassigning variable over and over.
    # TODO: Improve Formatting section.

    return output


def ErrorOut(source):
    return QtColorize(source, color=rgbToHex(200))


__all__ = member_loader.ListFunction(__name__)
