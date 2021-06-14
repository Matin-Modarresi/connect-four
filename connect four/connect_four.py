import copy
game_board = [['-' for i in range(7)]for j in range(7)]
game_board_copy=copy.deepcopy(game_board)

stop=0

def print2d(arr):
	for i in arr:
		print(*i,sep=' ')


def MAX(arr, row_col=[] ,index=0,rows=[6,6,6,6,6,6,6]):
	
	
	if stop_condition(arr,row_col,rows): 
		print2d(arr)
		return
	
		

	if index==49:
		print2d(arr)
		print()
		return

	#if stop==1 or stop==-1:
	#	stop=0
	#	return

	arr_send=[]
	rows_send=[]
	row_col_send=[]

	if index%2==0:
		for j in range(7):
			if rows[j]==-1:
				continue
			arr_copy = copy.deepcopy(arr)
			rows_copy=copy.deepcopy(rows)

			arr_copy[rows_copy[j]][j]='x'
			row_col_send.append(j)
			rows_copy[j]-=1
			arr_send.append(arr_copy)
			rows_send.append(rows_copy)
			
			
		count=0
		for arr in arr_send:
			MAX(arr,row_col_send[count],index+1,rows_send[count])
			count+=1

				
	else:
		for j in range(7):
			if rows[j]==-1:
				continue
			arr_copy = copy.deepcopy(arr)
			rows_copy=copy.deepcopy(rows)
			arr_copy[rows_copy[j]][j]='o'
			row_col_send.append(j)
			rows_copy[j]-=1
			arr_send.append(arr_copy)
			rows_send.append(rows_copy)
			

		count=0
		for arr in arr_send:
			MAX(arr,row_col_send[count],index+1,rows_send[count])
			count+=1
				



def stop_condition(arr,row,col):
	count_o=0
	count_x=0
	
	for i,j in zip(range(row,row+4),range(col,col+4)):
		if i==7 or j==7:
			break
		if arr[i][j]=='o':
			count_o+=1
		elif arr[i][j]=='x':
			count_x+=1
		else:
			break

	for i,j in zip(range(row,row-4,-1),range(col,col-4,-1)):
		if i==7 or j==7:
			break
		if arr[i][j]=='o':
			count_o+=1
		elif arr[i][j]=='x':
			count_x+=1
		else:
			break
	
	print(count_x,count_o)
	print(row,col)
	print()

	if count_o==4: 
		return -1

	if count_x==4: 
		return 1



	
	
	




	

	
	


MAX(game_board_copy)

#print2d(game_board)

