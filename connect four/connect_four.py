import copy
import coordinates as cor
import ctypes
import os

game_board = [['-' for i in range(7)]for j in range(7)]
game_board_copy=copy.deepcopy(game_board)

stop=0
char=''


def print2d(arr):
	for i in arr:
		print(*i,sep=' ')

class Node:
	def __init__(self,map):

		self.leaves=[]
		self.rows=[]
		self.value=0
		self.map=map
		self.row=0
		self.col=0
		self.status = 0
		
		self.detail_val ={ 'nozoli':0 , 'soudi':0, 'ofoghi':0 , 'amoodi':0}


	def insert(self,map):
		if self.map:
			self.leaves.append(Node(map))
		else:
			self.map=map


	def printTree_bfs(self):

		for j in self.leaves:
			print(round(j.value,2),end='\t\t')

		print()

		for i in self.detail_val:
			for j in self.leaves:
				print(f"{i:<6}",j.detail_val[i],end='\t')
			print()


		for i in range(7):
			for j in self.leaves:
				print(*j.map[i],end='\t')
			print()
		
			





def MAX(self,index=0,rows=[6,6,6,6,6,6,6],row=0,col=0):
	global last_level,stop_turn
	stop = stop_condition(self,row,col)
	
	self.rows=rows
	self.row=row
	self.col=col

	if stop==1: 
		self.value/=index
		return 1

	if stop==-1:
		self.value/=index
		return -1
	

	if index==stop_turn:
		last_level+=1
		return 0


	map_copy=[]
	rows_send=[]

	
	for j in range(7):
		if rows[j]==-1:
			continue

		map_copy = copy.deepcopy(self.map)
		rows_copy=copy.deepcopy(rows)

		if index%2==0:
			map_copy[rows_copy[j]][j]='x'
		else:
			map_copy[rows_copy[j]][j]='o'

		rows_copy[j]-=1
		self.leaves.append(Node(map_copy))
		ignore=MAX(self.leaves[-1],index+1,rows_copy,rows_copy[j]+1,j)
		
		#if ignore==1 or ignore==-1:
		#	break;
	
	if index%2==0:
		maximum = -1000000
		for i in self.leaves:
			if i.value > maximum:
				maximum = i.value
		
		self.value+=maximum

	else:
		minimum = 1000000
		for i in self.leaves:
			if i.value < minimum:
				minimum=i.value

		self.value+=minimum



	



def stop_condition(self,row,col):

	value=0
	range_  = [
			   [ [(row,row+4),(col,col+4)]      ,[(row-1,row-4,-1),(col-1,col-4,-1)] ],
			   [ [(row,row-4,-1),(col,col+4)]   ,[( row+1,row+4),(col-1,col-4,-1)]   ],
			   [ [(row,row+4),col]				,[(row-1,row-4,-1),col]				 ],
			   [ [row,(col,col+4)]				,[row,(col-1,col-4,-1)]				 ]
			  ]


	for i in range_:
		count = 0
		check = None
		self.value=0
		

		for j in i:
			check_=False
			if i==range_[0] or i==range_[1]:
				for n,m in zip(range(*j[0]),range(*j[1])):
					condition,count,check,check_ = conditions(self,n,m,count,check,check_)
					if not condition:
						break

				if i==range_[0]:
					self.detail_val['nozoli']=self.value

					
				else:
					self.detail_val['soudi'] =self.value
			
					

			
			if i==range_[2]:
				for n in range(*j[0]):
					condition,count,check,check_ = conditions(self,n,j[1],count,check,check_)
					if not condition:
						break

				self.detail_val['amoodi'] =self.value
	
				


			if i==range_[3]:
				for m in range(*j[1]):
					condition,count,check,check_ = conditions(self,j[0],m,count,check,check_)
					if not condition:
						break

				self.detail_val['ofoghi'] =self.value
				
				

		
		value+=self.value

		global turn

		if count>=4:
			self.status = 1
			self.value+=1000
			return 1

		if count<=-4:
			self.status =-1
			self.value-=1000
			return -1

	self.value=value
	return 0




	
def conditions(self,row,col,count,check,check_):

	
	
	if row>=7 or col>=7 or row<=-1 or col<=-1:
		return False,count,check,check_


	if self.map[row][col]=='-':
		if not check_:
			check_=True
		if check=='x':
			self.value += .5
		else:
			self.value-=.5





	if self.map[row][col]=='x':

		if check==None or check=='x':
			if check_:
				self.value+=1
			else:
				count+=1
				self.value+=1
				check='x'

		if check=='o':
			return False,count,check,check_

	
	
	if self.map[row][col]=='o':

		if check==None or check=='o':
			if check_:
				self.value-=1
			else:
				count-=1
				self.value-=1
				check='o'

		if check=='x':
			return False,count,check,check_

	return True,count,check,check_




	
	
column=None

last_level=0
turn = 0
stop_turn=5

game_finished = False

tree=Node(game_board_copy)
MAX(tree)
rows=[6,6,6,6,6,6,6]

while not game_finished:
	
	tree=Node(game_board_copy)
	MAX(tree,turn,rows)

	for i in range(turn,stop_turn):

		
		maximum=-1000000
		index=0
	
		print("select a column:")
		if i%2==0:
			for i in tree.leaves:
				if i.value>maximum:
					maximum=i.value
					index_max=index
				index+=1
			

			
			print(index_max)
			
			print(tree.row,tree.col)
			print(*tree.leaves[index_max].rows)
			print2d(tree.leaves[index_max].map)

			print()
	
			tree.printTree_bfs()
			
			print()

			tree.leaves[index_max].printTree_bfs()

			print()
		
			if tree.leaves[index_max].status==1:
				print("you lose")
				game_finished = True
				break

			tree=tree.leaves[index_max]

			cor.gotoxy(0,17)

			column=int(input())
	
		else:
			
			if 0 <= column < len(tree.leaves) and  tree.rows[column] is not -1:
	
					if tree.leaves[column].status == -1:
						print('you win')
						game_finished = True
						break
					print()

					tree=tree.leaves[column]
			else:
				print("please enter again")
				char=input()
			
		os.system("cls")

	game_board_copy=copy.deepcopy(tree.map)
	rows=tree.rows
	turn=stop_turn
	stop_turn+=5
	
	
	
