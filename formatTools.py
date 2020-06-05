
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
    lvl_array = [(r, 0, 0) for r in slicer(0, 255, 5)]

    return QtColorize(source, color=lvl_array[n])


def ErrorOut(source):
    return QtColorize(source, color=rgbToHex(200))
