
# Find Pattern in subfolder and output to
# {SubDir}_{Pattern}.txt
# Assume grep is in path
import os
import sys

rootdir = "."
if(len(sys.argv)<=3):
    print ("Usage:")
    print ("    py {} <Folder> <File> <Pattern1> <Pattern2> ...".format(os.path.basename(__file__)))
    sys.exit()

strFolderIn = sys.argv[1]
# if(strFolderIn[-1]!='\\'):
#     strFolderIn = strFolderIn + '\\'
strFileExt = sys.argv[2]

strPatterns = []
for i in range(3,len(sys.argv)):
    strPattern = sys.argv[i]
    strPatterns.append(strPattern)

for root, dirs, files in os.walk(strFolderIn):
    for d in dirs:
        for strPattern in strPatterns:
            cmd = "grep {Pattern} {DirIn}\\{SubDir}\\{File} > {SubDir}_{Pattern}.txt".format(Pattern=strPattern, DirIn=strFolderIn, SubDir=d, File=strFileExt)
            os.system(cmd)

