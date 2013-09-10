import sys;

fileName = sys.argv[ 1 ]
fileData = open( fileName, "r" )

count = 0
whiteSpace = ( "\n", " ", "\t" ]
aBlankLine = True

for line in fileData:
    if line[ 0 ] != "#":
        for c in line:
            if c not in whiteSpace:
                aBlankLine = False
                break
        if not aBlankLine:
            count += 1
            aBlankLine = True

print count

fileData.close()       