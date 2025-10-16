# import os

# print('Current Directory: ',os.getcwd())

#Create a folder inside current directory using python

# import os
# cdir=os.getcwd()
# folder_name=input('Enter folder name to create: ')
# folder_path=os.path.join(cdir,folder_name)
# if(os.path.exists(folder_path)):
#     print('Folder ALready Exist')
# else:
#     os.makedirs(folder_path,exist_ok=True)
#     print(f'{folder_name} created at {folder_path}')

#Rename a folder inside current directory using python
#Exercise
#You will take folderName from user
#if it exist, you will ask new name and rename it

# import os
# cdir=os.getcwd()
# old_name=input('Enter the folder name to rename:\t')
# new_name=input('Enter the new name of the folder: ')
# old_folder_path=os.path.join(cdir,old_name)
# new_folder_path=os.path.join(cdir,new_name)
# if os.path.exists(old_folder_path):
#     os.rename(old_folder_path,new_folder_path)
#     print(f'Folder rename from {old_name} to {new_name}')
# else:
#     print(f'{old_name} folder does not exist')

import calc
print('Average of 10,20 is:\t', calc.avg(10,20))
          
