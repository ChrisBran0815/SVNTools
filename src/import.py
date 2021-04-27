#!/usr/bin/env python3.9
import os

repo_path = 'https://svn.app.dmgmori.com/svn/DM-SH-AWT/V-Projects'
import_path = r'C:\Users\brandauc\Desktop\test'
comment = 'Auto Import'
for i in os.listdir(import_path):
    print(i)    
    folder_import = import_path + '/' + i
    repo_new_folder = repo_path + '/' + i
    print(folder_import)
    print(repo_new_folder)
    os.system(f'svn mkdir "{repo_new_folder}" -m "{comment}"')
    os.system(f'svn import "{folder_import}" "{repo_new_folder}" -m "{comment}')
   



