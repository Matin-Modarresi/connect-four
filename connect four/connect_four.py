import copy
game_board = [['-' for i in range(7)]for j in range(7)]
game_board_copy=copy.deepcopy(game_board)

stop=0
char=''

def print2d(arr):
	for i in arr:
		print(*i,sep=' ')

class Node:
	def __init__(self,data,value):

		self.leaves=[]
		self.data=data
		self.value=value

	def insert(self,data):
		if self.data:
			self.leaves.append(Node(data))
		else:
			self.data=data

	def printTree(self):
		for i in self.leaves:
			if i.data:
				print(i.value)
				print2d(i.data)
				print()
				i.printTree()
			


	

def MAX(arr,self,index=0,rows=[6,6,6,6,6,6,6],row=0,col=0):
	
	value=stop_condition(arr,row,col)
	
	self.leaves.append(Node(arr,value))
	#print(value)
	#print2d(arr)
	#print()
		
	if value==100: 
		print2d(arr)
		print()
		input(char)
		return 1

	if value==-100:
		print2d(arr)
		print()
		input(char)
		return -1
	

	if index==5:
		#print2d(arr)
		#print('ok')
		return 0

	#if stop==1 or stop==-1:
	#	stop=0
	#	return

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
		
		ignore=MAX(arr_copy,self.leaves[-1],index+1,rows_copy,rows_copy[j]+1,j)
		
		if ignore==1 or ignore==-1:
			break;
	

						



def stop_condition(arr,row,col):

	value=0
	count_o=0
	count_x=0
	check_o=True
	check_x=True

	for i,j in zip(range(row,row+4),range(col,col+4)):
		condition,count_x,count_o,check_x,check_o = conditions(arr,i,j,count_x,count_o,check_x,check_o)
		if(not condition):
			break
			
		

	for i,j in zip(range(row-1,row-4,-1),range(col-1,col-4,-1)):
		condition,count_x,count_o,check_x,check_o = conditions(arr,i,j,count_x,count_o,check_x,check_o)
		if(not condition):
			break

	if count_o<=-4:
		return -100
	else: value+=count_o

	if count_x>=4: 
		return 100
	else: value+=count_x

####################################################
	count_o=0
	count_x=0
	check_o=True
	check_x=True

	for i,j in zip(range(row,row-4,-1),range(col,col+4)):
		condition,count_x,count_o,check_x,check_o = conditions(arr,i,j,count_x,count_o,check_x,check_o)
		if(not condition):
			break
		

	for i,j in zip(range(row+1,row+4),range(col-1,col-4,-1)):
		condition,count_x,count_o,check_x,check_o = conditions(arr,i,j,count_x,count_o,check_x,check_o)
		if(not condition):
			break

	if count_o<=-4:
		return -100
	else: value+=count_o

	if count_x>=4: 
		return 100
	else: value+=count_x

###################################################	
	count_o=0
	count_x=0
	check_o=True
	check_x=True

	for i in range(row,row+4):
		condition,count_x,count_o,check_x,check_o = conditions(arr,i,col,count_x,count_o,check_x,check_o)
		if(not condition):
			break


	for i in range(row-1,row-4,-1):
		conditon,count_x,count_o,check_x,check_o = conditions(arr,i,col,count_x,count_o,check_x,check_o)
		if(not condition):
			break

	if count_o<=-4:
		return -100
	else: value+=count_o

	if count_x>=4: 
		return 100
	else: value+=count_x

##################################################
	count_o=0
	count_x=0
	check_o=True
	check_x=True

	for j in range(col,col+4):
		condition,count_x,count_o,check_x,check_o = conditions(arr,row,j,count_x,count_o,check_x,check_o)
		if(not condition):
			break



	for j in range(col-1,col-4,-1):
		condition,count_x,count_o,check_x,check_o = conditions(arr,row,j,count_x,count_o,check_x,check_o)
		if(not condition):
			break

	if count_o<=-4:
		return -100
	else: value+=count_o

	if count_x>=4: 
		return 100
	else: value+=count_x

	if value>0:
		return value-3
	elif value<0: 
		return value+3
	else:
		return 0




	
def conditions(arr,row,col,count_x, count_o,check_x,check_o):
	
	if row>=7 or col>=7 or row<=-1 or col<=-1:
		return False,count_x,count_o,check_x,check_o


	if arr[row][col]=='-':
		return False,count_x,count_o,check_x,check_o

	if arr[row][col]=='x' and check_x==False:
		return False,count_x,count_o,check_x,check_o

	if arr[row][col]=='o' and check_o==False:
		return False,count_x,count_o,check_x,check_o

	if arr[row][col]=='o' and check_o:
		count_o-=1
		check_x=False

	if arr[row][col]=='x' and check_x:
		count_x+=1
		check_o=False

	return True,count_x,count_o,check_x,check_o


def calc_value(arr,row, col,value):
	if row>=7 or col>=7:
		return False,count_x,count_o,check_x,check_o

	if row<=-1 or col<=-1:
		return False,count_x,count_o,check_x,check_o

	if arr[row][col]=='-':
		return False,count_x,count_o,check_x,check_o

	if arr[row][col]=='x' and check_x==False:
		return False,count_x,count_o,check_x,check_o

	if arr[row][col]=='o' and check_o==False:
		return False,count_x,count_o,check_x,check_o

	if arr[row][col]=='o' and check_o:
		count_o-=1
		check_x=False

	if arr[row][col]=='x' and check_x:
		count_x+=1
		check_o=False

	return True,count_x,count_o,check_x,check_o

tree=Node(game_board_copy,0)
MAX(game_board_copy,tree)
tree.printTree()



#print2d(game_board)

