import os
import re
import sys

# TODO: use check freeze state from python_img_macro
# TODO: create python script to grep all TODO in source codes.
# TODO: subitem by y-m-d => h-m-s order


def fileLineCounter(file):
    for idx, l in enumerate(file):
        pass

    return idx
    
    
def numericToAlphabet(total, index):
    def digit(num, base=10):
        if num == 0:
            return 0
        else:
            return digit(num//base) + 1
    
    out = '0'*(digit(total) - digit(index))
    
    if index == 0:
        return out
    else:
        return out + str(index)
    
    
def openWrapper(loc, mode='rt'):
    try:
        f = open(loc, mode)

    except FileNotFoundError:
        return False

    else:
        return f
    

def lineProcess(location, limit=-1, blacklist=['.*reqId.*', '.*url.*']):
    # Can I modularize this mess? not sure..
    # TODO: add color 2 hex function
    
    def swap(arr, idx1, idx2):
        arr[idx1], arr[idx2] = arr[idx2], arr[idx1]
        
    def colorize(text, size='8', weight='600', color='#000000'):
        Start = '<span style=\" '
        Font = f'font-size:{size}pt; '
        FontWeight = f'font-weight:{weight}; '
        Color = f'color:{color}; '
        End =  '\" >'
        txt = str(text)
        spanComplete = '</span>'
        
        return Start + Font + FontWeight + Color + End + txt + spanComplete
        
    # Won't happen when called via UI class
    # -------------------------------------
    file = openWrapper(location)
    if not file:
        print('filenotfound')
        return 0
    # -------------------------------------
    
    output = []
    file_end = fileLineCounter(openWrapper(location))
    # did this because python didn't process section 'with file' after passing to LineCounter
    
    with file as f:
        
        for line, text in enumerate(f):
            
            # checking this condition on every line doesn't sound great.
            if line == limit:
                break

            text_arr = text.split(',"')
            index = numericToAlphabet(file_end, line)
            item = [index]

            for idx, txt in enumerate(text_arr):
                
                # checking if txt contains blacklists
                # ----------------------------------
                remove = False
                
                for bl in blacklist:
                    if re.match(bl, txt):
                        remove = True
                        
                if remove:
                    continue
                else:
                    txt = re.sub('"', '', txt)
                # ----------------------------------

                if re.match('message', txt):
                    # Silly way of using regex, but more readable I guess.
                    msg = re.sub('message', '', txt)
                    msg = msg.replace(':', '', 1)
                    msg = msg.replace('\\', '/')
                    msg = re.sub('/+', '/', msg)
                    # msg = re.sub('/n#', '\n#', msg)
                    # This cause TreeItem extend to multiple lines, use only in Qtextbrowser
                    
                    item.append(msg)
                    
                else:

                    txt = re.sub('}', '', txt)
                    txt = re.sub(':', ',', txt, 1)
                    txt = re.sub('.*,', '', txt)
                    item.append(str(txt))
            
            swap(item, 1, 2)
            # item[2] = colorize(item[2], color='#ff0000')
            if item[3]=='':
                item[3] = '--'
            if item[5] == 'no app in context':
                item[5] = '--'
            output.append(item)

    return output
    
    
# Debugging function
if __name__ == '__main__':
    output = lineProcess('./testcase/owncloud.log', limit=30)
    if not isinstance(output, int):
        for txt in output:
            for i in txt:

                print('*' + i + '*')

    