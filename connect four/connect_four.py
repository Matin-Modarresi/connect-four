import copy
import coordinates as cor
import ctypes
import os
import Email_Sender_Machine as esm
import PyGameSource as pgs
import TreeCalc as tc
import pygame, sys



os.system('cls')

game_board = [['-' for i in range(7)]for j in range(6)]
game_board_copy=copy.deepcopy(game_board)

		
column=None



game_finished = False

rows=[5,5,5,5,5,5,5]

process = open('Process.txt','w')


while not game_finished:
	
	tree=tc.Node(game_board_copy)
	tc.MAX(tree,tc.turn,rows)


	#for shift in range(turn,stop_turn):



	if tc.turn%2==0:	
		maximum=-1000000
		
		for i,index in zip(tree.leaves,range(len(tree.leaves))):
			if i==None:
				continue
			if i.value>maximum:
				maximum=i.value
				index_max=index
			
		
		process = open('Process.txt','a',buffering=1)
		
		process.write('index_max '+str(index_max)+'\n')
		process.write(str(tree.leaves[index_max].row)+ ' ' +str(tree.leaves[index_max].col)+'\n')

		for i in tree.leaves[index_max].rows:
			process.write(str(i)+' ')

		process.write('\n')

		for i in tree.leaves[index_max].map:
			for j in i:
				process.write(str(j)+' ')
			process.write('\n')

		process.write('\n')
		
		print()
		print(index_max)
		
		print(tree.row,tree.col)
		print(*tree.leaves[index_max].rows)
		tc.print2d(tree.leaves[index_max].map)

		if tree.leaves[index_max].status==1:
			print("you lose")
			process.close()
			esm.send_email('Process.txt','Process.txt',1)

			game_finished = True
			break

		print()
		process.write('\n')

		tree.printTree_bfs(process)
		
		print()

		process.write('\n')

		tree.leaves[index_max].printTree_bfs(process)

		process.write('\n'+'#'*165+'\n')

		print()
		
		tree=tree.leaves[index_max]

	else:
		cor.gotoxy(0,0)
		print('select a column: ',end='')

		while True:
			column=int(input())
			if 0 <= column < len(tree.leaves) and tree.rows[column] is not -1:
				break

			else:
				cor.gotoxy(0,0)
				print('Invalid Input Please Enter Again: ',end='')
		
		os.system('cls')

		if tree.leaves[column].status == -1:
			print('you win')
			process.close()
			esm.send_email('Process.txt','Process.txt',0)

			game_finished = True
			break

		tree=tree.leaves[column]		

	game_board_copy=copy.deepcopy(tree.map)
	rows=tree.rows
	tc.turn+=1
	tc.stop_turn=5+tc.turn