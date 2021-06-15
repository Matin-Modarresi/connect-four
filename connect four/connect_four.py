import copy
game_board = [['-' for i in range(7)]for j in range(7)]
game_board_copy=copy.deepcopy(game_board)

stop=0

def print2d(arr):
	for i in arr:
		print(*i,sep=' ')


def MAX(arr,index=0,rows=[6,6,6,6,6,6,6],row=0,col=0):
	
	stop=stop_condition(arr,row,col)
	
	if stop==1: 
		print2d(arr)
		print()
		return

	if stop==-1:
		print2d(arr)
		print()
		return
	

	if index==49:
		#print2d(arr)
		#print('ok')
		return

	#if stop==1 or stop==-1:
	#	stop=0
	#	return

	arr_send=[]
	rows_send=[]
	

	if index%2==0:
		for j in range(7):
			if rows[j]==-1:
				continue
			arr_copy = copy.deepcopy(arr)
			rows_copy=copy.deepcopy(rows)

			arr_copy[rows_copy[j]][j]='x'
			rows_copy[j]-=1
			MAX(arr_copy,index+1,rows_copy,rows_copy[j]+1,j)
			

				
	else:
		for j in range(7):
			if rows[j]==-1:
				continue
			arr_copy = copy.deepcopy(arr)
			rows_copy=copy.deepcopy(rows)

			arr_copy[rows_copy[j]][j]='o'
			rows_copy[j]-=1
			MAX(arr_copy,index+1,rows_copy,rows_copy[j]+1,j)
			
			
				



def stop_condition(arr,row,col):

	count_o=0
	count_x=0
	check_o=True
	check_x=True

	for i,j in zip(range(row,row+4),range(col,col+4)):
		if i>=7 or j>=7:
			break
		if i<=-1 or j<=-1:
			break
		if arr[i][j]=='-':
			break
		if arr[i][j]=='x' and check_x==False:
			break
		if arr[i][j]=='o' and check_o==False:
			break

		if arr[i][j]=='o' and check_o:
			count_o+=1
			check_x=False

		if arr[i][j]=='x' and check_x:
			count_x+=1
			check_o=False
		

	for i,j in zip(range(row-1,row-4,-1),range(col-1,col-4,-1)):
		if i>=7 or j>=7:
			break
		if i<=-1 or j<=-1:
			break
		if arr[i][j]=='-':
			break
		if arr[i][j]=='x' and check_x==False:
			break
		if arr[i][j]=='o' and check_o==False:
			break

		if arr[i][j]=='o' and check_o:
			count_o+=1
			check_x=False

		if arr[i][j]=='x' and check_x:
			count_x+=1
			check_o=False



	if count_o>=4:
		print(count_x,count_o)
		print(row,col)
		print()
		return -1

	if count_x>=4: 
		print(count_x,count_o)
		print(row,col)
		print()
		return 1
####################################################
	count_o=0
	count_x=0
	check_o=True
	check_x=True

	for i,j in zip(range(row,row-4,-1),range(col,col+4)):
		if i>=7 or j>=7:
			break
		if i<=-1 or j<=-1:
			break
		if arr[i][j]=='-':
			break
		if arr[i][j]=='x' and check_x==False:
			break
		if arr[i][j]=='o' and check_o==False:
			break
		
		if arr[i][j]=='o' and check_o:
			count_o+=1
			check_x=False
		
		if arr[i][j]=='x' and check_x:
			count_x+=1
			check_o=False
		

	for i,j in zip(range(row+1,row+4),range(col-1,col-4,-1)):
		if i>=7 or j>=7:
			break
		if i<=-1 or j<=-1:
			break
		if arr[i][j]=='-':
			break
		if arr[i][j]=='x' and check_x==False:
			break
		if arr[i][j]=='o' and check_o==False:
			break

		if arr[i][j]=='o' and check_o:
			count_o+=1
			check_x=False

		if arr[i][j]=='x' and check_x:
			count_x+=1
			check_o=False


	if count_o>=4:
		print(count_x,count_o)
		print(row,col)
		print()
		return -1

	if count_x>=4: 
		print(count_x,count_o)
		print(row,col)
		print()
		return 1

###################################################	
	count_o=0
	count_x=0
	check_o=True
	check_x=True

	for i in range(row,row+4):
		if i>=7:
			break
		if i<=-1:
			break

		if arr[i][col]=='-':
			break
		if arr[i][col]=='x' and check_x==False:
			break
		if arr[i][col]=='o' and check_o==False:
			break

		if arr[i][col]=='o' and check_o:
			count_o+=1
			check_x=False

		if arr[i][col]=='x' and check_x:
			count_x+=1
			check_o=False




	for i in range(row-1,row-4,-1):
		if i>=7:
			break
		if i<=-1:
			break

		if arr[i][col]=='-':
			break
		if arr[i][col]=='x' and check_x==False:
			break
		if arr[i][col]=='o' and check_o==False:
			break

		if arr[i][col]=='o' and check_o:
			count_o+=1
			check_x=False

		if arr[i][col]=='x' and check_x:
			count_x+=1
			check_o=False

	if count_o>=4:
		print(count_x,count_o)
		print(row,col)
		print()
		return -1

	if count_x>=4: 
		print(count_x,count_o)
		print(row,col)
		print()
		return 1


##################################################
	count_o=0
	count_x=0
	check_o=True
	check_x=True

	for j in range(col,col+4):
		if j>=7:
			break
		if j<=-1:
			break

		if arr[row][j]=='-':
			break
		if arr[row][j]=='x' and check_x==False:
			break
		if arr[row][j]=='o' and check_o==False:
			break

		if arr[row][j]=='o' and check_o:
			count_o+=1
			check_x=False

		if arr[row][j]=='x' and check_x:
			count_x+=1
			check_o=False



	for j in range(col-1,col-4,-1):
		if j>=7:
			break
		if j<=-1:
			break

		if arr[row][j]=='-':
			break
		if arr[row][j]=='x' and check_x==False:
			break
		if arr[row][j]=='o' and check_o==False:
			break

		if arr[row][j]=='o' and check_o:
			count_o+=1
			check_x=False

		if arr[row][j]=='x' and check_x:
			count_x+=1
			check_o=False

	if count_o>=4:
		print(count_x,count_o)
		print(row,col)
		print()
		return -1

	if count_x>=4: 
		print(count_x,count_o)
		print(row,col)
		print()
		return 1

	"""if row==4 and col==5:
		print(count_x,count_o)
		print(row,col)
		print()
		return 1"""

	


MAX(game_board_copy)

#print2d(game_board)

