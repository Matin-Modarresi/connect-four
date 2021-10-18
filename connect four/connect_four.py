import copy
import coordinates as cor
import ctypes
import os
import Email_Sender_Machine as esm
import PyGameSource as pgs
import TreeCalc as tc
import pygame, sys
import math 
os.system('cls')



PI = math.pi
pygame.init()
os.system('cls')


windowSize = pygame.display.get_desktop_sizes()
print(windowSize)
window = pygame.display.set_mode(*windowSize)

boardW = 700
boardH = 600

window.fill((255,255,255))	
board = pgs.game_board(window,(windowSize[0][0]-boardW)/2,(windowSize[0][1]-boardH)/2,boardW,boardH,7,6)


board.set_color(0,23,0)
board.draw_board(window)
board.circle(window)



RED = (255,0,0)
BLUE = (0,0,255)
col_continue = 1
color_bead = RED


def show_game():
	while True:
		board.col_transparency(window)
		
		
		if board.selected_col != None and col_continue%30==0:
			board.beads(window,color_bead)
			board.selected_col = None
			color_bead = BLUE if color_bead is RED else RED
			pgs.start = False

			if col_continue>=1*30: break
	
			col_continue+=1
			
			
		col_continue += 1 if pgs.start else 0

	
		print(col_continue)
		for event in pygame.event.get():
			if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
				pygame.quit()
				sys.exit()

		pygame.display.update()




def start_game():
	global board, RED, BLUE, col_continue , color_bead , window

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
			
			board.selected_col = index_max
			board.beads(window,color_bead)
			color_bead = BLUE
			tree=tree.leaves[index_max]
			
	
		else:
			cor.gotoxy(0,0)
			print('select a column: ',end='')
	



				
			while True:
				board.col_transparency(window)
				
				
				if board.selected_col != None and col_continue%30==0:
					board.beads(window,color_bead)
					color_bead = BLUE if color_bead is RED else RED
					pgs.start = False

					if col_continue>=1*30: break
	
					col_continue+=1
					
					
				col_continue += 1 if pgs.start else 0

	
				
				pgs.exit_from_game()

				pygame.display.update()



			
			
			
	
			if tree.leaves[board.selected_col].status == -1:
				print('you win')
				process.close()
				esm.send_email('Process.txt','Process.txt',0)
	
				game_finished = True
				break
	
			tree=tree.leaves[board.selected_col]
			
		board.selected_col = None
		game_board_copy=copy.deepcopy(tree.map)
		rows=tree.rows
		tc.turn+=1
		tc.stop_turn=5+tc.turn


start_game()
#show_game()