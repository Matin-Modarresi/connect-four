import copy
game_board = [['-' for i in range(7)]for j in range(7)]

game_board_copy=copy.deepcopy(game_board)

def print2d(arr):
	for i in arr:
		print(i)

def MAX(arr, index=0,rows=[6,6,6,6,6,6,6]):
	#count=0
	#for i in rows:
	#	if i==0:
	#		count+=1
	#if count==6:
	#	return
	if index==7:
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
			print2d(arr_copy)
			print()
			
			arr_send.append(arr_copy)
			rows_send.append(rows_copy)
			#if rows[j]==-1: return

		for j in range(7):
			MAX(arr_send[j],index+1,rows_send[j])
	
	else:
		for j in range(7):
			if rows[j]==-1:
				continue
			arr_copy = copy.deepcopy(arr)
			rows_copy=copy.deepcopy(rows)
			arr_copy[rows_copy[j]][j]='o'
			rows_copy[j]-=1
			print2d(arr_copy)
			print()
			
			arr_send.append(arr_copy)
			rows_send.append(rows_copy)
			#if rows[j]==-1: return

		for j in range(7):
			MAX(arr_send[j],index+1,rows_send[j])
		

			

	


MAX(game_board_copy)

print()
#print2d(game_board)

