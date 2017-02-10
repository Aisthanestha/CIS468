#!/usr/bin/env python3
import json,argparse, zipfile
'''
Use argparse to tke the file  as a command line arg.
use -f
add a description
add the argparse help option
'''
#set parser for argparse 
parser=argparse.ArgumentParser(description='lab03.py will unzip file read in the data and output company name founding year and funding amounts')
#add an argument for the script to accept files, nargs creates bigger
parser.add_argument('-f','--file',help='Enter a file name',nargs='*')
#print help menu
parser.print_help()
#set to vars for now to prevent error
arg=vars(parser.parse_args())
'''
catches error if no arg values provided
'''
#catches if no arg.values  
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
        #extract the memeber companies .json
        zip.extract(file[1])
        with open(file[1]) as f:
        	#read in all lines to buffer of content
            content=f.readlines()
        #make a dict where we will store the company name
        company={}
        #read the content 
        for i in content:
            #set json load 
            x=json.loads(i)
            #find company within the json
            company=x['_id']['user']['company']
            #set the value of company to j
            company[funds]=j

#set file to arg.file so we can pass to functions
file=arg.file
#call this function with file as a var
diddlydo(file)
