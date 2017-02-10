#!/usr/bin/env python3
import zipfile

#with open('string.txt','r') as f:
#        content=f.read()
zip=zipfile.ZipFile('test.zip')

content=zip.namelist()
with open('string.txt')as f:
        printme=f.read()
print(printme)
