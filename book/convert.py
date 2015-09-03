from os import listdir
from os.path import isfile, join
import pdb

currPath = '.'
figsPath = './figs'

def main():
    origNames = [f.replace('_', ':').split('.')[0] for f in listdir(figsPath)]
    newNames = [f.split('.')[0] for f in listdir(figsPath)]
    filesToChange = [f for f in listdir(currPath) if isfile(join(currPath, f)) if f.endswith('.tex')]

    for f in filesToChange:
        for (origName, newName) in zip(origNames, newNames):
            with open(f, 'r') as h:
                origLines = h.read()
            with open(f, 'w') as h:
                h.write(origLines.replace(origName, newName))

if __name__ == '__main__':
    main()
