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


def Qtcolorize(text, color='#000000'):
    Start = '<span style=\" '
    # Font = f'font-size:{size}pt; '
    # FontWeight = f'font-weight:{weight}; '
    Color = f'color:{color}; '
    End =  '\" >'
    txt = str(text)
    spanComplete = '</span>'

    return Start + Color + End + txt + spanComplete


def lvlColorizer(source):
    
    def slicer(start, end, counts):
        steps = (end - start) // (counts - 1)
        for i in range(start, end + 1, steps):
            yield i
    
    n = int(source)
    lvlArray = [rgbToHex(r, 0, 0) for r in slicer(0, 255, 5)]
    
    return Qtcolorize(source, color=lvlArray[n])


def messageFormating(source):
    # what a mess, but can't do Qtcolorize('#\S*') at all!
    import re
    
    tmp = Qtcolorize('RRRR').split('RRRR')
    
    rowColor = rgbToHex(128)
    output = source.replace('/n#', '\n#')
    #output = re.sub('#\S*', '@@#``', output)
    
    #output = output.replace('@@', tmp[0])
    #output = output.replace('``', tmp[1])
    #output = output.replace('#', Qtcolorize('#'))
    
    return output


__all__ = member_loader.ListFunction(__name__)