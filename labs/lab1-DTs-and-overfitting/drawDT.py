from sys import stdout,argv
from os  import linesep

def readTree(h, str, indent):
    l = h.readline()
    if len(l) == 0:
        return

    for i in range(indent-1):
        stdout.write('|    ')
    if indent > 0:
        stdout.write('-')
        stdout.write(str)
        stdout.write('-> ')

    a = l.split()

    if l[0] == 'L':
        numPos = float(a[1])
        numNeg = float(a[2])
        acc    = float(int(1000*numPos/(numPos+numNeg)))/10.0
        print '%g%%\t(%d pos, %d neg)' % (acc, numPos, numNeg)
    elif l[0] == 'N':
        feat = a[1]
        stdout.write(feat)
        stdout.write(linesep)
        readTree(h, 'Y', indent+1)
        readTree(h, 'N', indent+1)
    else:
        raise Exception('malformed file')

def drawDT(filename):
    h = open(filename, 'r')

    numTrees = int(h.readline())
    for treeId in range(numTrees):
        treeWeight = float(h.readline())
        readTree(h, '', 0)
            
    h.close()
    
if __name__ == "__main__":
    if len(argv) != 2:
        print 'usage: python drawDT.py [filename]'
        exit(-1)
    drawDT(argv[1])
    
