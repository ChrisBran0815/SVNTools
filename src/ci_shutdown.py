#!/usr/bin/env python3.9
import os
import datetime
import time
import subprocess

def main():
    while True: 
        userin = input('You want Shutdown (s) or Restart (r) your System? (s/r)')
        if userin in ['R', 'r', 'S', 's']: break
    work_path = 'D:/SVN/V-Projekte'
    
    today = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M')) 
    msg = f'Auto Commit {today}'

    for work_copy in os.listdir(work_path):
        work_copy = work_path + '/' + work_copy
        check_for_add(work_copy)
        check_commit(work_copy, msg)
    
    time.sleep(5)    
    if userin in ['s', 'S']:
        os.system('shutdown.exe /s /t 00')
    elif userin in ['r', 'R']:
        os.system('shutdown.exe /r /t 00')   

def check_for_add(work_copy):
    os.system(f'svn add "{work_copy}" --force')

def check_commit(work_copy, msg):
    os.system(f'svn ci "{work_copy}" -m "{msg}"')
    print('Succsesfull commited')

if __name__ == '__main__':
    main()