#!/usr/bin/env python3
'''
Basically since this script is instructed to do a dir that you have i don't know what dir you want
so lets do it where i'm running the script from

path will be the variable i store the path from where the script is ran

to get the path and be able to work elsewhere if the filesystme isn' structuarlly similiar, i use
OS.GETCWD()

sideNote:
i think os.walk would have been better but didn't look into that too much
not sure though
'''
import os
path=os.getcwd()
'''
this shows a total of 5 files for me anyway
'''
foo=os.listdir(path)

'''
Basically i finished this, than OCD kicked in and i wanted to beautify it, instead of printing this ugly list lets make it awesome with where we print the bytes so remove this following print

print(foo)

On stackedoverflow i found different ways to do this but i made this way up and it worked
Since os.listdir(path) prints a list of ~4 files for me it will iterate through and print
the files sizes
'''
#used in for loop
x=0
print('\n')
for i in os.listdir(path):
        #let t be a variable holder for the size of the file in the path i is the file name 
        t=os.path.getsize(i)
        #this returns the size in bytes, yikes
        print(foo[x],t,'bytes')
        #lets iterate through the dir with this since we can't use the i in the for 
        x+=1
print('\n')
