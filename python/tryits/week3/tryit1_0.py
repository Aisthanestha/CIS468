#!/usr/bin/env python3
import zipfile
'''
this will create a zip file and write to it
'''
with open('string.txt','w+') as f:
        for i in range(0,10):
            f.write('hi this is a test\n')

zip=zipfile.ZipFile('test.zip','w')
zip.write('string.txt',compress_type=zipfile.ZIP_DEFLATED)



