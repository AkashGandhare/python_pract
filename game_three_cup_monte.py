#Author: Akash Gandhar
#Date: 22/09/2020
#Desc: Guess an index postion in a list

#import

from random import shuffle

#Function prototype

def shuffle_list(userList):
	shuffle(userList)
	return userList

def enterGuess():
	guess = input("enter a guess from '0', '1' or '2'\n")	
	while guess not in ['0','1','2']:		
		guess = input("enter a guess from '0', '1' or '2' \n")

	return int(guess);

def checkGuess(myList, guess):
	if myList[guess] == 'O':
		print("Correct")
		print(myList)
	else:
		print("Wrong")
		print(myList)


#Initial list
myList = ['O',' ',' ']

#Shuffle list
shuffle_list(myList)

#Ask for a guess to a user
userGuess = enterGuess()

#Check the guess with the list
checkGuess(myList,userGuess)