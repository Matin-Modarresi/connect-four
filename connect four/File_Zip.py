import os
from zipfile import ZipFile
main_dir = os.getcwd()

def get_all_file_paths(directory):
  
    file_paths = []
  
    for root, directories, files in os.walk(directory):
        for filename in files:
         
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)
  
    
    return file_paths



def zip(zip_name,root,file_loc=os.getcwd(),save_loc=os.getcwd(),delete=False):

    os.chdir(file_loc)
    file_paths = get_all_file_paths(root)
    
    
    with ZipFile(zip_name,'w') as zipf:
        for file in file_paths:
            zipf.write(file)

    os.chdir(main_dir)

#    move_command = 'move ' + zip_name + ' ' + "\"" + save_loc + "\""
#    os.system(move_command)

    if delete:
        os.chdir(file_loc)
        del_command = 'del '+ root + '/s /q'
        os.system(del_command)

    os.chdir(main_dir)


def unzip(zip_name, zip_loc=os.getcwd() , delete=False):

    os.chdir(zip_loc)
    with ZipFile(zip_name,'r') as zipf:
        zipf.extractall()
    

    if delete:
        del_command = 'del ' + zip_name +'/s /q'
        os.system(del_command)
    os.chdir(main_dir)
