#!/usr/bin/env python3.9
import subprocess, os
import datetime
import getpass

def main():
    
    repo_path = 'file:///C:/Users/chris/Documents/testrepo/Projekte'
    work_path = r'C:\Users\chris\Desktop\Projekte'

    #Check if the folder {work_path} exist if not create
    if not os.path.exists(work_path):
        os.makedirs(work_path)
        
    while True:
        vnum = input('Enter the V-Number: ')
        if not vnum == '':
            break
    while True:
        custname = input('Enter the Customer Name: ')
        if not custname == '':
            break
    projname = 'VT_' + vnum + '_' + custname.replace(' ', '_')
    work_path = work_path + '/' + projname
    new_project = repo_path + '/' + projname
    comment = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M'))
    comment = f'{comment} created by {getpass.getuser()}'
    
    os.system(f'svn mkdir {new_project} -m "{comment}"')

    os.system(f'svn checkout "{new_project}" "{work_path}"')
    pass

if __name__ == '__main__':
    main()