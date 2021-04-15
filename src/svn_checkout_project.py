#!/usr/bin/env python3.9
import subprocess
import os

def main():
    
    path = 'file:///B:/020_Department/A-tech/AWT/Daten Mitarbeiter/Brandau, Christoph/_Projekte/V_Projekte'
    work_path = 'D:/SVN/V-Projekte'
    project_lst = []
    find_lst = []

    #Check if the folder {work_path} exist if not create
    if not os.path.exists(work_path):
        os.makedirs(work_path)

    #Check all Projects in the SVN {path}
    status = subprocess.run(f'svn list "{path}"', stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    
    #Append all Projects to the list 
    for content in status.stdout.splitlines():
        project_lst.append(content)
    
    #Enter String to search the project
    while True:
        os.system('cls')
        search = input('Enter Projekt: ')
        if search != '': break
    
    #Append all all projects which contain the {search} string to the list
    for i in project_lst:
        if search in i:
            find_lst.append(i)
    
    #Print all projects t console which contain the {search} string
    if len(find_lst) > 0:
        i = 0
        for content in find_lst:
            i += 1
            print(f'{str(i)}. {str(content).replace("/","")}')
    else:
        print('No Project found. Please Create one!')
        os.system('pause')
        return
    
    #Choose the project which should be checked out if more then 1 result was found
    if len(find_lst) > 1:
        while True:
            try:
                checkout_num = input('Please enter the Number from the Project which you want checkout: ')
                checkout_num = int(checkout_num)
                if checkout_num <= len(find_lst):
                    if type(checkout_num) == int:
                        checkout_path = path + '/' + find_lst[checkout_num-1] #os.path.join(path, find_lst[int(checkout_num)-1])
                        break
                else:
                    print('Please enter a right Number!')
                    os.system('pause')
            except:
                print('Please enter a right Number!')
                os.system('pause')
                continue
    else:
        checkout_num = 1
        checkout_path = path + '/' + find_lst[checkout_num-1]

    #Ask if you want check out the Project
    while True:
        os.system('cls')
        checkout = input(f'You are sure to checkout {find_lst[checkout_num-1]}? (Y/N) ')
        if checkout in ['N', 'n']: 
            break
        elif checkout in ['Y', 'y']:
            work_path = work_path + '/' + find_lst[checkout_num-1]
            os.system(f'svn checkout "{checkout_path}" "{work_path}"')
            break

if __name__ == '__main__':
    main()