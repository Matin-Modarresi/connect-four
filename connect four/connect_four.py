import copy
game_board = [['-' for i in range(7)]for j in range(7)]
game_board_copy=copy.deepcopy(game_board)

stop=0
char=''

def print2d(arr):
	for i in arr:
		print(*i,sep=' ')

class Node:
	def __init__(self,data):

		self.leaves=[]
		self.data=data

	def insert(self,data):
		if self.data:
			self.leaves.append(Node(data))
		else:
			self.data=data

	def printTree(self):
		for i in self.leaves:
			if i.data:
				print2d(i.data)
				print()
				i.printTree()
			



def MAX(arr,self,index=0,rows=[6,6,6,6,6,6,6],row=0,col=0):
	
	stop=stop_condition(arr,row,col)
	
	
	if stop==1: 
		print2d(arr)
		print()
		input(char)
		return 1

	if stop==-1:
		print2d(arr)
		print()
		input(char)
		return -1
	

	if index==49:
		print2d(arr)
		print()
		return 0


	arr_send=[]
	rows_send=[]
	
	for j in range(7):
		if rows[j]==-1:
			continue
		arr_copy = copy.deepcopy(arr)
		rows_copy=copy.deepcopy(rows)

		if index%2==0:
			arr_copy[rows_copy[j]][j]='x'
		else:
			arr_copy[rows_copy[j]][j]='o'

		rows_copy[j]-=1
		self.leaves.append(Node(arr_copy))
		ignore=MAX(arr_copy,self.leaves[-1],index+1,rows_copy,rows_copy[j]+1,j)
		
		if ignore==1 or ignore==-1:
			break;
	

						



def stop_condition(arr,row,col):

	count = 0
	check =None

	for i,j in zip(range(row,row+4),range(col,col+4)):
		condition,count,check = conditions(arr,i,j,count,check)
		if(not condition):
			break
			
		

	for i,j in zip(range(row-1,row-4,-1),range(col-1,col-4,-1)):
		condition,count,check = conditions(arr,i,j,count,check)
		if(not condition):
			break

	if count>=4:
		print(count)
		print(row,col)
		if check=='x':
			return 1
		else:
			return -1

####################################################
	count=0
	check=None

	for i,j in zip(range(row,row-4,-1),range(col,col+4)):
		condition,count,check = conditions(arr,i,j,count,check)
		if(not condition):
			break
		

	for i,j in zip(range(row+1,row+4),range(col-1,col-4,-1)):
		condition,count,check= conditions(arr,i,j,count,check)
		if(not condition):
			break

	if count>=4:
		print(count)
		print(row,col)
		if check=='x':
			return 1
		else:
			return -1

###################################################	
	count=0
	check=None

	for i in range(row,row+4):
		condition,coutn,check= conditions(arr,i,col,count,check)
		if(not condition):
			break


	for i in range(row-1,row-4,-1):
		conditon,count,check = conditions(arr,i,col,count,check)
		if(not condition):
			break

	if count>=4:
		print(count)
		print(row,col)
		if check=='x':
			return 1
		else:
			return -1

##################################################
	count=0
	check=None

	for j in range(col,col+4):
		condition,count,check = conditions(arr,row,j,count,check)
		if(not condition):
			break



	for j in range(col-1,col-4,-1):
		condition,count,check = conditions(arr,row,j,count,check)
		if(not condition):
			break

	if count>=4:
		print(count)
		print(row,col)
		if check=='x':
			return 1
		else:
			return -1



	
def conditions(arr,row,col,count,check):
	
	if row>=7 or col>=7:
		return False,count,check

	if row<=-1 or col<=-1:
		return False,count,check

	if arr[row][col]=='-':
		return False,count,check

	if arr[row][col]=='x':

		if check== None or check=='x':
		   count+=1
		   check='x'
		else:
			return False,count,check

	if arr[row][col]=='o':

		if check==None or check=='o':
			count+=1
			check='o'
		else:
			return False,count,check

	return True,count,check


tree=Node(game_board_copy)
MAX(game_board_copy,tree)
#tree.printTree()



#print2d(game_board)

