import copy
game_board = [['-' for i in range(7)]for j in range(7)]
game_board_copy=copy.deepcopy(game_board)

count_o=0	
count_x=0
stop=0

def print2d(arr):
	for i in arr:
		print(i)


def MAX(arr, index=0,rows=[6,6,6,6,6,6,6]):
	
	if index==49:
		print2d(arr)
		print()
		return

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
			arr_send.append(arr_copy)
			rows_send.append(rows_copy)
			
			
		count=0
		for arr in arr_send:
			MAX(arr,index+1,rows_send[count])
			count+=1

				
	else:
		for j in range(7):
			if rows[j]==-1:
				continue
			arr_copy = copy.deepcopy(arr)
			rows_copy=copy.deepcopy(rows)
			arr_copy[rows_copy[j]][j]='o'
			rows_copy[j]-=1
			arr_send.append(arr_copy)
			rows_send.append(rows_copy)
			

		count=0
		for arr in arr_send:
			MAX(arr,index+1,rows_send[count])
			count+=1
				

count_o=0	
count_x=0
stop=0
def stop_condition(arr,row,col):
	
	if row==7 or col==7:
		return
	if stop==-1 or stop==1:
		return

	if arr[row][col]=='o':
		count_o+=1
	elif arr[row][col]=='x':
		count_x+=1
	else:
		return

	if count_o==4:
		stop = -1
	if count_x==4:
		stop = 1
	

	stop_condition(arr,row,col+1)
	stop_condition(arr,row+1,col+1)
	stop_condition(arr,row+1,col)
	stop_condition(arr,row,col-1)
	stop_condition(arr,row-1,col-1)
	stop_condition(arr,row-1,col)
	stop_condition(arr,row-1,col+1)
	stop_condition(arr,row+1,col-1)


	

	
	


#MAX(game_board_copy)

#print2d(game_board)

