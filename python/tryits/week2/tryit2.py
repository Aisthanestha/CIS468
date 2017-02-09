#!/usr/bin/env python
def averager(var):
        var=list(map(int, var))
        #this will add them together
        sum(var)
        #this will tell us the # of values in the list
        len(var)
        #basic math
        avg=float(sum(var)/len(var))
        return avg
                        
                        
                        
                        
#make variable in dict a list so we can add stuff to it
hisScore = ['100','95','68','84']
myScore=['100','100','100']
#create dict, name is key hiscore and myscore are lists to be able to append
students={'tyler': hisScore, 'greg': myScore}
#lets make an entry, to my understanding []
studentName=input('Enter the student name: ')
#check if in dict
#throws error score does not exist otherwise
score=''
#check if studentName is within students key list
if studentName in students.keys():
        #prints current values of whatever student was chosen
        print(students.get(studentName))
        #while score doesn't equal q keep adding 
        while score!='q':
            #take user input for the score you are going to add
            score=input('What was your score,[q] to quit: ')
            #this if statement prevents q being appended to the list
            if score!='q':
            #we got this far lets add what our input was to the list    
                    students[studentName].append(score)
#lets them know if it is not a student
else:
        print('invalid key')
var=students[studentName]
averaged=averager(var)
print(averaged)


#prints the dictionary so we can see what happened
#print(students)
