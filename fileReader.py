import re

# TODO: use check freeze state from python_img_macro
# TODO: create python script to grep all TODO in source codes.
# TODO: subitem by y-m-d => h-m-s order


def fileLineCounter(file):
    global lineCounts
    
    for idx, l in enumerate(file):
        pass
    
    lineCounts = idx
    return idx
    
    
def numericToAlphabet(total, lineIndex):
    def digit(num, base=10):
        if num == 0:
            return 0
        else:
            return digit(num//base) + 1
    
    out = '0'*(digit(total) - digit(lineIndex))
    
    if lineIndex == 0:
        return out
    else:
        return out + str(lineIndex)
    
    
def openWrapper(loc, mode='rt'):
    try:
        f = open(loc, mode)

    except FileNotFoundError:
        return 0
    else:
        return f
    

def lineProcess(location, limit=-1, blacklist=['.*reqId.*', '.*url.*']):
    # Can I modularize this mess? not sure..
    # TODO: add color 2 hex function

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
        output = []

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
                    
                    item.append(msg)
                    
                else:

                    txt = re.sub('}', '', txt)
                    txt = re.sub(':', ',', txt, 1)
                    txt = re.sub('.*,', '', txt)
                    item.append(str(txt))
            
            # Post process
            swap(item, 1, 2)
            
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

global lineCounts