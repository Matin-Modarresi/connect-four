import pygame,sys
import math , time
from colorama import Fore,init
init(convert=1)

PI=math.pi
pygame.init()



class game_board:

	def __init__(self,win,x,y,leng,wid,col,row):
		self.squares = [[]for i in range(row)]
		self.check_trans = [False for i in range(col)]
		self.check_squares = True
		self.x = x
		self.y = y
		self.selected_col = None
		self.length = leng
		self.width = wid
		self.col = col
		self.row = row
		self.col_space = self.partitations(self.length, self.col , 50)
		self.row_space = self.partitations(self.width , self.row , 50)
		self.last_bead=[0 for i in range(col)]

		self.rectTransH = (self.row-1)*self.row_space[1]+self.row*self.row_space[0]
		self.rectTransW = self.col_space[0]
		self.recTrans = [pygame.Surface((self.rectTransW,self.rectTransH)) for i in range(col)]

		##############################################################################################
		squareX = self.x+self.col_space[1]+self.col_space[2]/2
		squareY = self.y+self.row_space[1]+self.row_space[2]/2

		for i in range(self.row):
			for j in range(self.col):
				s = pygame.Surface((self.col_space[0],self.row_space[0]))  # the size of your rect
				s.fill((255,0,255))           
				pygame.draw.rect(s,(255,255,255),(0,0,self.col_space[0],self.row_space[0]),border_radius=100)
				s.set_colorkey((255,0,255))
				win.blit(s, (squareX,squareY)) 	
				
				self.squares[i].append((squareX,squareY,s))
				

				squareX+= self.col_space[0]+self.col_space[1]

			squareY += self.row_space[0] + self.row_space[1]
			squareX = self.x+self.col_space[1]+self.col_space[2]/2
		
		
		
		for i in range(self.row):
			for j in range(self.col):
				print('(',round(self.squares[i][j][0],2), round(self.squares[i][j][1],2), ')' , end=' ')
			print()
				
		self.check_squares = False

		print(Fore.RED+str(self.col_space))
		print(self.row_space)
		print(Fore.WHITE)
		
		

	def set_color(self,r,g,b):
		self.board_color = r,g,b

	def partitations(self,leng , table,border):

		space = leng/(table+1)
		leng -= (space+border)
		leng /= (table)
		space/= (table+1)
		return (leng,space,border)

	def circle (self,win):
		for i in self.squares:
			for j in i:
				win.blit(j[2],(j[0],j[1]))
				

	def col_transparency(self,win):

		for i,col in zip(self.squares[0],range(self.col)):
			if i[0] < pygame.mouse.get_pos()[0] < i[0]+self.col_space[0] and i[1]< pygame.mouse.get_pos()[1]< i[1]+self.rectTransH :
				if self.recTrans[col].get_alpha() != 50 :
					self.draw_board(win)
					self.circle(win)
					self.recTrans[col].fill((255,255,255))
					self.recTrans[col].set_alpha(50)
					self.check_trans[col]=True
					win.blit(self.recTrans[col],(i[0],i[1]))
					
					
				if pygame.mouse.get_pressed()[0] and self.last_bead[col]!=self.row:
					self.draw_board(win)
					self.circle(win)
					self.recTrans[col].set_alpha(80)
					#time.sleep(.01)
					win.blit(self.recTrans[col],(i[0],i[1]))
					self.selected_col = col
					
					


			else:
				if self.check_trans[col]:
					self.draw_board(win)
					self.circle(win)
					self.check_trans[col]=False
					self.recTrans[col].set_alpha(0)
				
				


		

		#print(rectTransH,self.length)


	def draw_board(self,window):
		
		self.board_rect = (window,(self.board_color),(self.x,self.y,self.length,self.width),0,20)
		pygame.draw.rect(*self.board_rect)
		
	
	
	def beads(self,win,color_bead):

		z = 0
		if self.last_bead[self.selected_col]==self.row-1:
			z=1
			print(Fore.GREEN+ str(self.last_bead[self.selected_col]))
			
		for fir_col,sec_col in zip(self.squares,self.squares[1-z:self.row-self.last_bead[self.selected_col]]):
			for j in range(-int(self.row_space[1]),int(self.row_space[0]),4):




				temp_fir = fir_col[self.selected_col][2].copy()
				temp_sec = sec_col[self.selected_col][2].copy()
				win.fill((255,255,255))
				
				self.draw_board(win)
				self.circle(win)
				pygame.draw.rect(temp_fir,color_bead,(0,j,self.col_space[0], self.row_space[0]),0,100)
				pygame.draw.ellipse(temp_fir,self.board_color,(0-16,0-16,self.col_space[0]+32,self.row_space[0]+32),16)

				pygame.draw.rect(temp_sec,color_bead,(0,j-self.row_space[1]-self.row_space[0],self.col_space[0], self.row_space[0]),0,100)
				pygame.draw.ellipse(temp_sec,self.board_color,(0-16,0-16,self.col_space[0]+32,self.row_space[0]+32),16)

				win.blit(temp_fir,(fir_col[self.selected_col][0],fir_col[self.selected_col][1]))
				win.blit(temp_sec,(sec_col[self.selected_col][0],sec_col[self.selected_col][1]))
				pygame.display.update()
				#time.sleep(.1)
		else:
			
			for j in range(-int(self.row_space[1]),int(self.row_space[0]),4):
				self.draw_board(win)
				self.circle(win)
				pygame.draw.rect(sec_col[self.selected_col][2],color_bead,(0,j,self.col_space[0], self.row_space[0]),0,100)
				pygame.draw.ellipse(sec_col[self.selected_col][2],self.board_color,(0-16,0-16,self.col_space[0]+32,self.row_space[0]+32),16)
				pygame.display.update()

			
			self.last_bead[self.selected_col]+=1


		
				

			for event in pygame.event.get():
				if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
					pygame.quit()
					sys.exit()
		

				

		


class game_player():

	def __init__(self , color,board):
		self.color = color



	def set_col(self, col):
		self.x_bead = game_board.squares[0][game_board.selected_col][0]
		self.y_bead = 0
		s = pygame.Surface((game_board.col_space[0],game_board.row_space[0]))  # the size of your rect

		
		s.fill((255,0,255))           
		pygame.draw.rect(s,(255,255,255),(0,0,game_board.col_space[0],game_board.row_space[0]),border_radius=100)
		win.blit(s,(self.x_bead,self.y_bead))
		self.y_bead+=10
		
		
	
