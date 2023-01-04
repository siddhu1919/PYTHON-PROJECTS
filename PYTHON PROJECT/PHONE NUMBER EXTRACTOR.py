#EXTRACTING PHONE NUMBER FROM A GIVEN TEXT (India)
import math as m
string="hello i'm Developer my num : 9194040089 and 7347484590 and 374848,47584929"


def extract_num(str):
	num1=""
	for i in str:

		if(i.isdigit()):
				num1+=i
	l=len(num1)
	count=int(m.ceil(len(num1)/10))
	#print(count)
	a=0
	last=10
	for x in range(0,count):
				print("Number {} :- {}".format(x+1,num1[a:last]))
				a=last
				last+=10
				
	#print("Number 1 : {}".format(num1))		
	

print(string)
extract_num(string)