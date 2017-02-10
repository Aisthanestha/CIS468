#!/usr/bin/env python3
import argparse,zipfile
'''
this will create a zip file and write to it
'''
def read(file):
        with open(file[0],'w') as f:
                for i in range(0,10):
                    f.write('WOW, great moves ethan keep it up!\n')

        zip=zipfile.ZipFile(file[1],'w')
        zip.write(file[0],compress_type=zipfile.ZIP_DEFLATED)
        zip.close()

def write(file):
        zip=zipfile.ZipFile(file[1])

        content=zip.namelist()
        with open(file[0])as f:
                    printme=f.read()
        print(printme)
        zip.close()




parser=argparse.ArgumentParser(description='This will read/write and zip files',epilog='This opens a file specified in the first -f arg value and writes the text from above into the file. Providing a 2nd file name it will zip into a desired name there.for example python3 test2.py -f test.txt test.zip, the program will open and write to test.txt and zip test.txt to a zip called test.zip')
parser.add_argument('-f','--file', help='Enter file to be written to THEN file to be zipped',nargs='+')
parser.print_help()
arg=vars(parser.parse_args())

if not any(arg.values()):
        parser.error('no args provided.')
arg=parser.parse_args()
read(arg.file)
write(arg.file)

