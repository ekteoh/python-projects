import os
import time
import random

board=[" "," "," "," "," "," "," "," "," "," "]
p1_board=[0,0,0,0,0,0,0,0,0,0]
p2_board=[0,0,0,0,0,0,0,0,0,0]

def print_header():
	print ("TIC-TAC-TOE")
	print (" \  /  /--\ ")
	print ("  \/   |  | ")
	print ("  /\   |  | ")
	print (" /  \  \--/ ")
	print ("1|2|3")
	print ("4|5|6")
	print ("7|8|9")

def print_board(board):
	print ("   |   |   ")
	print (" "+board[1]+" | "+board[2]+" | "+board[3]+"  ")
	print ("   |   |   ")
	print ("---|---|---")
	print ("   |   |   ")
	print (" "+board[4]+" | "+board[5]+" | "+board[6]+"  ")
	print ("   |   |   ")
	print ("---|---|---")
	print ("   |   |   ")
	print (" "+board[7]+" | "+board[8]+" | "+board[9]+"  ")
	print ("   |   |   ")

def result(board):
	h1=board[1]+board[2]+board[3]
	h2=board[4]+board[5]+board[6]
	h3=board[7]+board[8]+board[9]
	v1=board[1]+board[4]+board[7]
	v2=board[2]+board[5]+board[8]
	v3=board[3]+board[6]+board[9]
	d1=board[1]+board[5]+board[9]
	d2=board[3]+board[5]+board[7]
	if h1==3 or h2==3 or h3==3 or v1==3 or v2==3 or v3==3 or d1==3 or d2==3:
		return 1

def winner(p_board):
	if result(p_board)==1:
		print (p_board)
		return 1
	else:
		return 0

round=1
while winner(p1_board)==0 and winner(p2_board)==0:
	os.system("cls")
	print_header()
	print_board(board)
	print ("\nRound ",round)
	p1=int(input("P1's turn?(1-9)\n"))
	board[p1]="X"
	p1_board[p1]=1
	if result(p1_board)==1:
		os.system("cls")
		print_header()
		print_board(board)
		print ("\nRound ",round)
		board[p1]="X"
		print ("P1 is winner!")
		break
	
	os.system("cls")
	print_header()
	print_board(board)
	print ("\nRound ",round)
	p2=int(input("P2's turn?(1-9)\n"))
	board[p2]="O"
	p2_board[p2]=1
	if result(p2_board)==1:
		os.system("cls")
		print_header()
		print_board(board)
		print ("\nRound ",round)
		board[p1]="X"
		print ("P2 is winner!")
		break
	round+=1
	
	

	







