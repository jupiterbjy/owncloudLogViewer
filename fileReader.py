import re


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
    

def lineProcess(location, limit=-1, blacklist=None):
    # Can I modularize this mess? not sure..
    # TODO: add color 2 hex function

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

global lineCounts