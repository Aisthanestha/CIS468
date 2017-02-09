#!/usr/bin/env python3
#import json lib
import json
#open tweets.json default r
with open('tweets.json') as f:
        #read in lines as strings u''
        data=f.readlines()
#create tz as a set
tz=set()
for i in data:
        x=json.loads(i)
        #json object =x
        #instead of typing x['usr.... enter t as that
        t=x['user']['time_zone']
        #adds t to the set
        tz.add(t)



#this prints the set 
#print(tz)

#lets see how many we get
num=len(tz)
print('\n# of Time Zones:%s' %num)
num1=len(tz)-1
#that didn't seem right as NONE isn't a real timezone
#so i just removed 1 as NONE =1 in the nnumber of timezones
print('\nNote that NONE is a timezone listed in the tweets.json, without this it is a total of %s\n' %num1)
#print('\ni am also assuming that Arizona, as it is listed in the json as is an time zone itself aswell')
for i in tz:
        print(i)
