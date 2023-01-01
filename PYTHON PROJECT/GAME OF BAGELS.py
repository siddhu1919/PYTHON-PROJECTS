# The Game OF Bagels

'''RULES OF THE GAME
Bagels, a deductive logic game.

Created By Siddharth G Singh


<---   Guess a 3-digit number   --->


          Here are some clues:

PROMPT       :         That means:

Pico               :        One digit is correct but in the wrong position.

Fermi             :        One digit is correct and in the right position.

Bagels           :        No digit is correct.



 You have Only 10 guesses to get The Correct 3 Digit Number
'''

import random as r
import sys

clues=["pico","fermi","bagles"]
max_guess=10
max_digit=3
input_num=""

			

# FUNCTION FOR GENERATING 3 DIGIT RANDOM NUMBER

def rand_3digit(max_digit):
  number=r.randint(100,999)
  return number
  #print(number)
  
# FUNCTION FOR GIVING CLUE
def getting_clue(input_temp,temp_no):
	temp_1=temp_no[0]
	temp_2=temp_no[1]
	temp_3=temp_no[2]
	#print(temp_1,temp_2 ,temp_3)
	
	# FOR CORRECT GUESS
	if(input_temp==temp_no):
		print("AI > CONGRATS ! YOU HAVE SUCCEFULLY GUESSED THE NUMBER" )
		print("Correct Ans : {}".format(temp_no))		
		input()
		sys.exit()
		
	for i in range(len(input_temp)):
	 if input_temp[i] == temp_no[i]:
	 	print("Fermi")
	 elif input_temp[i] in temp_no:
	 	print("Pico")
	 else:
	 	print("Bagles")	
	 
	 



def main():
	print('''Bagels, a deductive logic game.

I am thinking of a 3 -digit number with  repeated digit
s.

Try to guess what it is. Here are some clues:
	

When I say    :     That means:

Pico.              |      One digit is correct but in                               the wrong position.
Fermi             |      One digit is correct and in                           the right position.

Bagels           |      No digit is correct.


For example, if the secret number was 248 and your guess was 843, the
clues would be Fermi Pico.\n\n''')
	secret_num=str(rand_3digit(max_digit))
	#print(secret_num)
	print("Pls Enter Only Digit Error !\n")
	for i in range(1, max_guess+1):
		input_num=str(input("#Guess {}> ENTER YOUR NUMBER : ".format(i)))
		getting_clue(input_num,secret_num)
		if i==10:
			print("Right Ans : {}\nYou Lose ! ....".format(secret_num))
	 	
	 
	
if __name__=='__main__':
	main()