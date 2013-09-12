import sys;

fileName = sys.argv[ 1 ]
fileData = open( fileName, "r" )

count = 0;
whiteSpace = [ "\n", " ", "\t" ]

for line in fileData:
    if line[ 0 ] != "#":
        for c in line:
            if c not in whiteSpace:
                count += 1
                break

print count

fileData.close()
    
