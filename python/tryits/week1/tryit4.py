#/usr/bin/python3
'''
create a script that has a function that creates a user inputted amount of random numbers
create other functions that calculate {sum, min, max, avg, median}
'''
#call libs
import random, math, statistics

def randomNum():
        #declare ran_array as a list
        ran_array=list()
        #ask user how many numbers we want for random
        ran=input("how many numbers do you want in total:")
        genornot="1"
        genornot=input("1.generate random numbers or 2.enter your own?[1]")
        if genornot == "1":
                for i in range(int(ran)):
                    ran=random.randrange(0,1000)
                    ran_array.append(int(ran))
        elif genornot == "2":
                for i in range(int(ran)):
                    #make user enter random number until loop is done
                    ran=input("Input a number:")
                    ran_array.append(int(ran))
        else:
                for i in range(int(ran)):
                        ran=random.randrange(0,1000)
                        ran_array.append(int(ran))
                
        print("ARRAY:",ran_array)
        return ran_array
def sumFunc(ran_array):
        #sum together ran_array
        sumAns=math.fsum(ran_array)
        return sumAns
def minFunc(ran_array):
        #find the minimum number in ran_array
        minAns=min(ran_array)
        return minAns
def maxFunc(ran_array):
        #find the max of the array:
        maxAns=max(ran_array)
        return maxAns
def avgFunc(ran_array):
        #use library statisitics to find the mean
        avgAns=statistics.mean(ran_array)
        return avgAns
def medianFunc(ran_array):
        #use library statistics to find the median
        medianAns=statistics.median(ran_array)
        return medianAns
#declare start of script for bug solving if needed
print("Start of script...\n\n")
ran_array=randomNum()
#Use this to verify you have ran_array in main
#print("This is the array within main: \n",ran_array)
print("\n")
sumAns=sumFunc(ran_array)
#Use this to print the sum of ran_array from randomNum function
print("The sum of your ran array is: ",sumAns)
print("\n")
minAns=minFunc(ran_array)
#Use this to print the smallest number in your array
print("The minimum number in your array is: ",minAns)
print("\n")
maxAns=maxFunc(ran_array)
#Use this to print the largest number in your array
print("The maximum number in the array is: ",maxAns)
print("\n")
avgAns=avgFunc(ran_array)
#Use this to print the average number in your array as an integer
print("the average of the array is: ", int(avgAns))
print("\n")
medianAns=medianFunc(ran_array)
#Use this to print the median of the array as an integer
print("The median of of the array is: ", int(medianAns))
print("\n")
#declare end of script
print("End of script...\n\n")
