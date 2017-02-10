#!/usr/bin/env python3
import json
import pprint 
file='companies.json'
with open(file,'r') as fin:
        content=fin.read()

formatted=pprint.pformat(content)
with open(file,'w') as fout:
        fout.write(formatted)
