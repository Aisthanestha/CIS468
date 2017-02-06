#!/usr/bin/python

import random

def numGenerator():
        lis=list()
        for x in range(0,4):
                lis.append(random.randint(0,1000))
        tup1=tuple(lis)        
        return tup1


nums=numGenerator()
print(nums)
#print(type(nums))
