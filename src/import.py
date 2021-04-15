#!/usr/bin/env python3.9
import os


repo_path = 'file:///B:/020_Department/A-tech/AWT/Daten Mitarbeiter/Brandau, Christoph/_Projekte/V_Projekte'
import_path = r'C:\Users\brandauc\Desktop\New folder\new'
comment = 'Auto Import'
for i in os.listdir(import_path):
    print(i)    
    folder_import = import_path + '/' + i
    repo_new_folder = repo_path + '/' + i
    print(folder_import)
    print(repo_new_folder)
    os.system(f'svn mkdir "{repo_new_folder}" -m "{comment}"')
    os.system(f'svn import "{folder_import}" "{repo_new_folder}" -m "{comment}')
   



