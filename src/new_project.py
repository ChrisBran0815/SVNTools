#!/usr/bin/env python3.9
import subprocess, os, sys
import shutil
import datetime
import time
import getpass

def main():
    
    repo_path = r'https://svn.app.dmgmori.com/svn/DM-SH-AWT/V-Projects'
    work_path = 'D:/SVN/V-Projekte'
    template = os.path.abspath("./template/")

    #Check if the folder {work_path} exist if not create
    if not os.path.exists(work_path):
        os.makedirs(work_path)

    while True:
        vnum = input('Enter the V-Number: ')
        if not vnum == '':
            if len(vnum) == 11:
                break
    while True:
        custname = input('Enter the Customer Name: ')
        if not custname == '':
            break
    projname = 'VT_' + vnum + '_' + custname.replace(' ', '_')
    work_path = work_path + '/' + projname
    new_project = repo_path + '/' + projname
    checkout = new_project + '/trunk'
    comment = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M'))
    comment = f'{comment} created by {getpass.getuser()}'
    print(new_project)
    os.system(f'svn mkdir "{new_project}" -m "{comment}"')
    os.system(f'svn import "{template}" "{new_project}" -m "Test"')
    os.system(f'svn checkout "{checkout}" "{work_path}"')
    
if __name__ == '__main__':    
    main()