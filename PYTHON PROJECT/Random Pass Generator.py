# Password Generator
import random as r
import sys


def passgen(num):
		if(num==1):
			print("Invalid Input !")
			sys.exit()
		else:
			char_list=["a","b","c","A","%","_","@",'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '#', '$', '=', ':', '?', '.', '/', '|', '~', '>','*', '(', ')', '<']
			for i in range(0,num):
				print(r.choice(char_list),end="")	
			
#__Main__

while True:
	passgen(int(input("ENTER THE LENGTH OF PASSWORD(Max 11 Characters) : ")))
	input()



	   	
	   	
 
	   	
	   	
    	
		