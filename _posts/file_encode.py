import os
from urllib import parse

rootDir = '.'
for dirName, subdirList, fileList in os.walk(rootDir):
    print('Found directory: %s' % dirName)
    for fname in fileList:
        print('\t%s' % fname)
        name = fname.split(".")[0]
        extension = fname.split(".")[1]
        if parse.quote(name) != name:
            try:
                os.rename(dirName+"\\" + fname,dirName+"\\" + parse.quote(name) + "." + extension)
            except:
                print("failed:", dirName+"\\" + fname)
