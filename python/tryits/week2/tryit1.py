#!/usr/bin/python
#imports for use of random.randint
import random
#fucntion to create random nums
def numGenerator():
        #declar lis as a  list
        lis=list()
        #run it 4 time and append an int into the list
        for x in range(0,4):
                lis.append(random.randint(0,1000))
        #this makes our lis which was a list to a tuple!
        tup1=tuple(lis)        
        #return the tuple
        return tup1

#nums equals the tup1 since thats what it returned
nums=numGenerator()
#print the nums from numGenerator
print(nums)
#print(type(nums))
