#Program To Reverse Any Natural Number

num = int(input("Enter Any Number : "))

rev_num=0

while num>0:
	rem=num%10
	rev_num=rev_num*10+rem 
	num //=10

print("Reversed Number : ",rev_num)