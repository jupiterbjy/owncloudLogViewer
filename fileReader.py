import os
import sys

def setwdir():
    os.chdir(sys.path[0])
            
def fileRead(location, mode='rt'):
    try:
        file = open(location, mode)
    except Exception as err:
        print(err)
        return 0  #fail condition
    else:
        return file

def lineProcess(file):
    try:
        with file as f:
            output = []
            for line, text in enumerate(f):
                if line < 50:
                    tmp = text.split(',')
                    #tmp[-2] = ''
                    for txt in tmp:
                        if 'url' in txt:
                            continue
                        elif 'Trace' in txt:
                            continue
                        else:
                            b = '\\'
                            a = txt.split(b*3)
                            out = ''.join(a)
                            output.append(out.replace('\\\\n', '\n\n'))

                    output.append('\n\n\n')
    except Exception as exp
        print(exp)
                
    return output