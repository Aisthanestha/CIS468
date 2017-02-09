#!/usr/bin/env python3
#import json lib
import json
#open tweets.json default r
with open('tweets.json') as f:
        #read in lines as strings u''
        data=f.readlines()
'''
#create tz as a set
tz=set()
for i in data:
        x=json.loads(i)
        #json object =x
        #instead of typing x['usr.... enter t as that
        t=x['user']['time_zone']
        #adds t to the set
        tz.add(t)
'''
#add to a dictionary not a set >.>
tz={}
for i in data:
        x=json.loads(i)
        t=x['user']['time_zone']
        #takes t and adds it to the dictionary timezone will be the key and 1 will be its value but the value of the key is irrelevant in this case...
        tz[t]=1
'''
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

'''
# to see the keys 
#print(tz.keys())
num=len(tz.keys())
print('\n')
print('Total Number of time Zones:%s\n'%num)
num-=1
print('If NONE is considered not a TIMEZONE:%s\n'%num)


for i in tz:
        print(i)
