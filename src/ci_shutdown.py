#!/usr/bin/env python3.9
import os
import datetime
import time
import subprocess

def main():
    while True: 
        userin = input('You want Shutdown (s) or Restart (r) your System? (s/r)')
        if userin in ['R', 'r', 'S', 's']: break
    path = r"D:\_Projekte"
    today = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M')) 
    msg = f'Auto Commit {today}'
    check_for_add(path)
    os.system(f'svn ci {path} -m "{msg}"')
    print('Succsesfull commited')
    time.sleep(5)    
    if userin in ['s', 'S']:
        os.system('shutdown.exe /s /t 00')
    elif userin in ['r', 'R']:
        os.system('shutdown.exe /r /t 00')   

def check_for_add(path):
    status = subprocess.run(f'svn status "{path}"', stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

    for status in status.stdout.splitlines():
        if status[0] == '?':
            sts = status.replace('?', '').strip()
            os.system(f'svn add "{sts}"')
    pass

def check_for_revert(path):
    
    status = subprocess.run(f'svn status "{path}"', stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

    for status in status.stdout.splitlines():
        if status[0] == '!':
            sts = status.replace('!', '').strip()
            #while True:
                #revert = input(f'You want revert {sts} (Y/N)')
                #if revert in ['N', 'n', 'Y', 'y']: break
            #if revert in ['N', 'n']: return
            os.system(f'svn revert "{sts}"')
            time.sleep(2)

if __name__ == '__main__':
    main()