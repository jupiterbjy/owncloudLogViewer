import os
import re
import sys

# TODO: use check freeze state from python_img_macro
# TODO: create python script to grep all TODO in source codes.
# TODO: subitem by y-m-d => h-m-s order

def setwdir():
    os.chdir(sys.path[0])


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
        return -1

    else:
        return f
    

def lineProcess(location, limit=-1):
    
    def swap(arr, idx1, idx2):
        arr[idx1], arr[idx2] = arr[idx2], arr[idx1]
        
    # Won't happen when called via UI class
    # -------------------------------------
    file = openWrapper(location)
    if file == -1:
        print('filenotfound')
        return 0
    # -------------------------------------
    
    blacklist = ['.*reqId.*', '.*url.*']
    output = []
    file_end = fileLineCounter(openWrapper(location))
    # did this because python didn't process 'with file' after tossing file to LineCounter
    
    with file as f:
        
        for line, text in enumerate(f):
            
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
                    # Add more processing to message section
                    msg = re.sub('message', '', txt)
                    msg = msg.replace(':', '', 1)
                    
                    item.append(msg)

                else:
                    txt = re.sub('}', '', txt)
                    txt = re.sub(':', ',', txt, 1)
                    txt = re.sub('.*,', '', txt)
                    item.append(str(txt))
            
            swap(item, 1, 2)
            if item[3]=='':
                item[3] = '--'
            if item[5] == 'no app in context':
                item[5] = '--'
            output.append(item)

    return output
    
    
# Testing function

if __name__ == '__main__':
    output = lineProcess('./log/owncloud.log', limit=30)
    for txt in output:
        for i in txt:

            print('*' + i + '*')
    
    