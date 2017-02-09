#!/usr/bin/env python3
'''
function to test startswith()
Determines if string or a substring of string (if starting index beg and ending index end are given) starts with substring str; returns true if so and false otherwise.

lets do it
'''
def starter(userInput,checker):
        #return tested, true or false
        tested=userInput.startswith(checker)
        return tested

'''
Function to test endswith()
Determines if string or a substring of string (if starting index beg and ending index end are given) ends with suffix; returns true if so and false otherwise.


'''
def ender(userInput,checker):
        #return tested, true or false
        tested=userInput.endswith(checker)
        return tested





'''
This one merges (concatanates) a sequence of strings 

for example seq= 'a' 'b' 'c'
s=''
s.join(seq)
print(s)
'abc'


for this brief func i will not take user input like the others


the function should return a-b-c-d below

i coudn't get the function to save the sequnce but was able to get it printed
'''
def join():
        #dash variable contains a space to be injected inbetween the chars of sequence from joinMe into one string
        dash=' '
        joinMe=('a','e','s','t','h','e','t','i','c')
        print(joinMe)
        #to be called later, joins with a space
        tested=dash.join(joinMe)
        return tested



'''
splits a single string into seperate strings
'''
def split():
        #string to be split
        splitMe='me no like this'
        print('\n',splitMe)
        #split string equals func to be called later
        tested=splitMe.split()
        return tested




'''
this will do rstrip lstrip and strip
organically strip does r strip and lstrip so redundant but for learning purposes

.rstrip() Removes all trailing whitespace of string.
.lstrip()Removes all leading whitespace of string.

.strip() does both rstrip&lstrip

'''
def strippers():
        print('\n')
        leading='     leading spaces'
        print(leading)
        trailing='trailing spaces     '
        print(trailing,'for clarity')
        both='   leading&trailingspaces   '
        print(both,'for clarity')
        print(leading.lstrip())
        print(trailing.rstrip(),'for clarity')
        print(both.strip(),'for clarity')
        print('\n')



'''
take user input for both the string to be tested and the character you will check against the string, userInput being the string
and checker being the characterr to be checked against the string
'''
userInput=input('\nEnter a string to be tested:')
checker=input('Enter a character that will check if string begins with:')
checker1=input('Enter a character that will check if string ends with:')
#print the checker user inputed and if it is false or true
print('Starts with an %s:'%checker,starter(userInput,checker))
#print the checker user inputed and if it is false or true
print('Ends with an %s:'%checker,ender(userInput,checker))
#run split and print return
print('\n%s'%join())
#print the return of split and run split
print(split())
#all prints done within func
strippers()














