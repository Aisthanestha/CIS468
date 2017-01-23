#!/usr/bin/python3
#GREGORY R. HENDRICKSON
'''
Read a single integer, n, from stdin
calculate the number of twin prime pairs between 1 and n
print the result to stdout
comments where necessary
    no comments points will be deducted!!!

TEST THIS SHIT BEFORE SUBMISSION, SILLY
'''
'''
A twin prime is a prime number that differs from another prime number by exactly two. For example, there are 8 prime pairs between 1 and 100

(3,5) | (5,7) | (11,13) | and so on
'''
'''
Submission Reqs.
Submit they .py file to d2l by deadline
push your .py file to your gitlab repo by deadline
add a short readme,md to repo
'''
'''
example of program 
$ python3 twin_prime.py
Enter number: 100
Result: 8
'''
import math

def isPrime(a):
        '''
        This function should take a single parameter
        and return True if "a" is a prime or False if "a" is not a prime
        '''
        
        if a==2 or a==3:
                return True
        # Number mod 2 = 0 then is not prime if num is less than 2 is not a prime
        if a%2 ==0 or a<2:
                return False
        #
        for i in range(3, int(math.sqrt(a))+1, 2):
                if a%i ==0:
                        return False
        return True

def main():
        '''
        This function should read a number, n, from stdin
        and print the number of twin prime pairs between 
        1 and "n".
        '''
        #read user input and store in n
        n=int(input("Enter Number: "))
        #primeNums=list()
        #create a list called nums to store numbers
        #start a loop to see if the number is prime
        for a in range(n):
                isPrime(a)
                #commented out below because used this for verification purposes
                #if isPrime(a) == True:
                        #good to see what is returned as a prime within a list
                        #primeNums.append(int(a))
        #print(primeNums)
        result=0
        
        for x in range(n):
                if isPrime(x) and isPrime(x+2) == True:
                        #prints pair
                        #print(x , x+2)
                        result+=1
        #print out result
        print("Result: ",result)


#calls main func
main()
