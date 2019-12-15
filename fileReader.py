import sys
import member_loader

def readFile(file):
    with open(file, 'wt') as f:
        for line in f:
            pass

            
exc = []
member_loader.ListFunction(__name__, blacklist=exc)
