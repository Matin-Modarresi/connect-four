import copy
game_board = [['-' for i in range(7)]for j in range(7)]

game_board_copy=copy.deepcopy(game_board)

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
			#print2d(arr_copy)
			
			#for r in rows_copy: print(f"{str(r):^5}",end='')
			#print('\n')
			arr_send.append(arr_copy)
			rows_send.append(rows_copy)
			#if rows[j]==-1: return
			
		count=0
		for arr in arr_send:
			MAX(arr,index+1,rows_send[count])
			count+=1

			#MAX(arr_copy,index+1,rows_copy)	
	else:
		for j in range(7):
			if rows[j]==-1:
				continue
			arr_copy = copy.deepcopy(arr)
			rows_copy=copy.deepcopy(rows)
			arr_copy[rows_copy[j]][j]='o'
			rows_copy[j]-=1
			#print2d(arr_copy)
			#for r in rows_copy: print(f"{str(r):^5}",end='')
			#print('\n')
			arr_send.append(arr_copy)
			rows_send.append(rows_copy)
			
			#if rows[j]==-1: return
        
		count=0
		for arr in arr_send:
			MAX(arr,index+1,rows_send[count])
			count+=1
			#MAX(arr_copy,index+1,rows_copy)	
		

	
	


MAX(game_board_copy)

#print2d(game_board)

