import member_loader

def rgbToHex(r=0, g=0, b=0):
    arr = [r, g, b]
    out = []
    for i in arr:
        if i < 16:
            out.append('0' + str(hex(i))[2:])
        else:
            out.append(str(hex(i))[2:])
    return '#' + ''.join(out)


def Qtcolorize(text, color='#000000', size=0, weight=0):
    Start = '<span style=\" '
    Font = f'font-size:{size}pt; '
    FontWeight = f'font-weight:{weight}; '
    Color = f'color:{color}; '
    End =  '\" >'
    txt = str(text)
    spanComplete = '</span>'
    
    out = [Start, Font, FontWeight, Color, End, txt, spanComplete]
    
    if not size:
        out.remove(Font)
    
    if not weight:
        out.remove(FontWeight)

    return ''.join(out)


def lvlColorizer(source):
    
    def slicer(start, end, counts):
        steps = (end - start) // (counts - 1)
        for i in range(start, end + 1, steps):
            yield i
    
    n = int(source)
    lvlArray = [rgbToHex(r, 0, 0) for r in slicer(0, 255, 5)]
    
    return Qtcolorize(source, color=lvlArray[n])


def messageFormating(source, color=True):
    import re
    
    matching = re.findall('#\S*', source)
    rowColor = rgbToHex(200)
    output = source[::]
    
    if color:
        for case in matching:
            output = output.replace(case, Qtcolorize(case, rowColor), 1)
    
        output = output.replace('/n<', '<br/><')
        
    else:
        output = output.replace('/n#', '<br/>#')
        
    output = output.replace('#0', '<br/>#0')
    
    return output

def ErrorOut(source):
    return Qtcolorize(source, color=rgbToHex(200))


__all__ = member_loader.ListFunction(__name__)
