#NUMBER TO WORDS
#GLOBAL 
number=['zero','one','two','three','four','five','six','seven','eight','nine']

def num2words(num):
	if(num==0):
		return " "
	else:
		digit=number[num%10]
		word=str(num2words(int(num/10)))+str(digit)+" "
		
	return word	
	
print(num2words(int(input("\nEnter The Number : "))))
