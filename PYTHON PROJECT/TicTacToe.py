#Tic Tac Toe 

import random as r
import sys

win_cases=[[1,2,3],[4,5,6],[7,8,9],[1,5,9],[7,5,3],[1,4,7],[2,5,8],[3,6,9]]

user_case=[]
bot_case=[]
game=[ [" - ", " - "," - "],[" - ", " - "," - "],[" - ", " - "," - "]]
chance=0

row =[]
col=[]
pos=[]

# Bot chance

def bot():
		posx=[]
		posy=[]
		x=r.randint(0,2)
		y=r.randint(0,2)
		posx.append(x)
		posy.append(y)
		temp = zip(posx,posy)
		temp = list(temp)
		if (temp not in pos):
			pos.append(temp)
			game[x][y]=' O '
		else:
			bot()

# user chance

def userchance():
	
	temp1 = int(input("\n> Choose Destination Row : "))
	
	temp2 = int(input("\n> Choose Destination Column : "))
	posx=[]
	posy =[]
	posx.append(temp1)
	posy.append(temp2)
	t= zip(posx,posy)
	t=list(t)
	
	if (t not in pos ):
		pos.append(t)
		if (temp1<0 or temp1>2)and temp2<0 or temp2>2:
			print("\nThis Isn't Fair bro ! \nEnter appropriate Place ^⁠_⁠^")
			userchance()
		else:
			game[temp1][temp2]=' x '
			user_case.append([temp1,temp2])
			win(game)
		#print(game)
	else:
		print("\n--------------- Invalid choice --------------- \n")
		showboard(game)
		userchance()
		
		
		
#  show board 

def showboard(game):
	print()
	#game= [ [0,0,0],[0,0,0],[0,0,0] ]	
	for i in range (0,3):
		for j in range(0,3):
			print(game [i][j]," ",end="")
			
		print("\n")

def win(game):
	if(game[0][0] ==' x ' and game[0][1]==' x ' and game[0][2]==' x ' or game[1][0]==' x ' and game[1][1] ==' x 'and game[1][2]==' x ' or game[2][0] ==' x 'and game[2][1] ==' x 'and game[2][2] ==' x 'or game[0][0]==' x ' and game[1][1] ==' x 'and game[2][2]==" x "):
		showboard(game)
		print("Hurray ! You won ^⁠_⁠^")
		sys.exit()
		
	elif(game[0][0] ==' O ' and game[0][1]=='  O ' and game[0][2]==' O ' or game[1][0]==' O ' and game[1][1] ==' O 'and game[1][2]==' O ' or game[1][0] ==' O 'and game[1][1] ==' O 'and game[1][2] ==' O 'or game[2][0]==' O ' and game[2][1] ==' O 'and game[2][2]==" O "):
		print("Bot Wins ! Better Luck Next Time ")
		sys.exit()
		
	
#pcchance()
#userchance()

def main():
	user=1
	chance=1
	
	while True:
		win(game)
		showboard(game)
		if(user==1):
			print("\n> Your chance ......\n")
			userchance()
			user-=1
			chance+=1
			#print(game)			
		else:
			bot()
			#showboard(game)
			user+=1
			chance+=1
			
			
			


if __name__=='__main__':
 main()
 