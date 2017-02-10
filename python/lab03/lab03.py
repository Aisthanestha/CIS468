#!/usr/bin/env python3
import json,argparse, zipfile
'''
Use argparse to tke the file  as a command line arg.
use -f
add a description
add the argparse help option
'''

parser=argparse.ArgumentParser(description='lab03.py will unzip file read in the data and output company name founding year and funding amounts')
parser.add_argument('-f','--file',help='Enter a file name',nargs='*')
parser.print_help()
#set to vars for now to prevent error
arg=vars(parser.parse_args())
'''
catches error if no arg values provided
'''
if not any(arg.values()):
        parser.error('no args provided.')
#removed vars
arg=parser.parse_args()
'''
read stuff into the file
'''
def diddlydo(file):
        #opens up the zip file specified at the arg[0]
        zip=zipfile.ZipFile(file[0])
        zip.extract('companies.json')
        with open(file[1]) as f:
        	content=f.readlines()
        company={}
        for i in content:
        	x=json.loads(i)
        	company=x['_id']['user']['company']
        	comp[company]='1'


file=arg.file
diddlydo(file)
#print(file)
comp={}
