import copy
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
		self.value=0
		self.map=map
		self.row=0
		self.col=0
		self.nozoli=0
		self.soudi=0
		self.ofoghi=0
		self.amoodi=0

	def insert(self,map):
		if self.map:
			self.leaves.append(Node(map))
		else:
			self.map=map

	def printTree(self):
		for i in self.leaves:
			if i.map:
				print(i.row,i.col)
				print2d(i.map)
				print()
				i.printTree()
			



def MAX(self,index=0,rows=[6,6,6,6,6,6,6],row=0,col=0):
	
	stop = stop_condition(self,row,col)

	self.row=row
	self.col=col
	
	print(self.value)
	print(self.row,self.col)
	#print(count)
	print2d(self.map)
	print()
	input(char)

	if stop==1: 
		#print(self.value)
		#print(self.row,self.col)
		##print(count)
		#print2d(self.map)
		#print()
		#input(char)
		return 1

	if stop==-1:
		#print2d(self.map)
		#print()
		#input(char)
		return -1
	

	if index==5:
		#print2d(arr)
		#print()
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
		
		if ignore==1 or ignore==-1:
			break;
	

						



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

					if i==range_[0]:
						self.nozoli=self.value
					else:
						self.soudi=self.value

					if not condition:
						break
			
			if i==range_[2]:
				for n in range(*j[0]):
					condition,count,check,check_ = conditions(self,n,j[1],count,check,check_)
					self.ofoghi=self.value

					if not condition:
						break


			if i==range_[3]:
				for m in range(*j[1]):
					condition,count,check,check_ = conditions(self,j[0],m,count,check,check_)
					self.amoodi=self.value

					if not condition:
						break

		
		if i==range_[0]:
			print("nozoli: " ,count,self.value)
			value+=self.value
		elif i==range_[1]:
			print("soudi:  ",count,self.value)
			value+=self.value
		elif i==range_[2]:
			print("amoodi: ",count,self.value)
			value+=self.value
		else:
			print("ofoghi: ",count,self.value)
			value+=self.value	

		if count>=4:
			self.value+=100
			if check=='x':
				return 1
			else:
				return -1

	self.value=value
	return 0




	
def conditions(self,row,col,count,check,check_):

	
	
	if row>=7 or col>=7 or row<=-1 or col<=-1:
		return False,count,check,check_


	if self.map[row][col]=='-':
		if not check_:
				check_=True
				self.value += count+.5
		else: self.value+=.5


	if self.map[row][col]=='x':

		#if check=='x' and check_:


		if check==None or check=='x':
			if check_:
				self.value+=1
			else:
				count+=1
				check='x'


		if check=='o':
			return False,count,check,check_

	if self.map[row][col]=='o':

		if check==None or check=='o':
			if check_:
				self.value+=1
			else:
				count+=1
				check='o'


		if check=='x':
			return False,count,check,check_

	return True,count,check,check_


tree=Node(game_board_copy)
MAX(tree)
#tree.printTree()



#print2d(game_board)

