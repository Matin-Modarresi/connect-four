#get value for set losser or winner
import File_Controller as fc
import Email_Server as es
import File_Zip as fz
import os

#os.chdir('"Game Resault"')


def send_email(text_file, new_text, game_resault):

	counter_file = open('counter.txt','r')
	
	code_text=counter_file.readlines()

	
	string = str()
	
	if game_resault:
		for i in code_text[0]:
			if i=='\n':
				break
			string += i
		
		fc.file_controller(text_file , new_text ,string,'Games-Resault/root/winner')
		code_text[0]=str(int(string)+1)+'\n'
		
	
	else:
		fc.file_controller(text_file , new_text ,code_text[1], 'Games-Resault/root/losser')
		code_text[1]=str(int(code_text[1])+1)
	
	counter_file.close()

	counter_file = open('counter.txt','w')
	counter_file.writelines(code_text)
	counter_file.close()
	
	subject        = "An email with attachment from Python"
	body           = "This is an email with attachment sent from Python"
	sender_email   = "developermatin1378@gmail.com"
	receiver_email = "developermatin1378@gmail.com"
	password       = "Mod!_1378"
	
	
	fz.zip('Games-Resault.zip','root','Games-Resault','Games-Resault',True)
	
	try:
		os.chdir('Games-Resault')
		es.email_sender(subject,body,'Games-Resault.zip',sender_email,receiver_email,password)
	
	except:
		os.chdir(fz.main_dir)
		fz.unzip('Games-Resault.zip','Games-Resault',True)
			