# text.txt , Directroy that should be move files on it , name string , type
import os

def file_controller( file_name, new_file_name , text_code, new_path ,old_path=os.getcwd()):

	os.chdir(old_path)

	check = True
	name , type_of_file = '',''

	for i in new_file_name:
		if i=='.':
			check = False
		if check:
			name += i
		else:
			type_of_file+=i

	new_file_name = name +'-'+ text_code + type_of_file

	ren_command =  "rename " + file_name + ' ' + new_file_name
	move_command = "move " +  new_file_name + ' ' + new_path 

	os.system(ren_command)
	os.system(move_command)
