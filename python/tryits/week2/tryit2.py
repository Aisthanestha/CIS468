import statistics

def average(Students{}):
        print(statistics.mean.Students['tyler'])

scoreInput=''
Students={'tyler':[10,100,340,20,10],'greg':[100,100,54,72,57]}
#pprint.pprint(Students)

print(Students.keys())

userInput=input('Enter a students name, q to quit: ')

if userInput in Students.keys():
        scoreInput=input('Enter the score for the student: ')

elif userInput == 'q':
        print()
else:
        print('Invalid Key')
average(Students)
