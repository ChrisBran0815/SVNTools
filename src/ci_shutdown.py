import os
import subprocess
import platform
import time
import zipapp


def add(item):
    cmd = ' '.join([f'svn add "{item}" --force'])
    subprocess.run(cmd, stdout=subprocess.PIPE,
                   stderr=subprocess.PIPE, universal_newlines=True)


def commit(item, msg):
    cmd = ' '.join([f'svn ci {item} -m "{msg}"'])
    ci = subprocess.run(cmd, stdout=subprocess.PIPE, shell=True,
                        stderr=subprocess.PIPE, universal_newlines=True)
    for info in ci.stdout.splitlines():
        print(info)


def remove(item):
    cmd = ' '.join(f'svn rm {item}')
    subprocess.run(cmd, stdout=subprocess.PIPE,
                   stderr=subprocess.PIPE, universal_newlines=True)


def svn_func():

    if platform.system() == 'Linux':
        path = '/home/christoph/Dokumente/test/trunk'
    elif platform.system() == 'Windows':
        path = r'D:\SVN\V-Projekte'

    for wc in os.listdir(path):
        wc = os.path.join(path, wc)
        cmd = " ".join(['svn st', wc])
        output = subprocess.run(
            cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        for status in output.stdout.splitlines():
            item = status[8:]
            if status[:1] == '!':
                remove(item=item)
                continue
            elif status[:1] == 'A':
                continue
            elif status[:1] == '?':
                add(item=item)
                continue
            elif status[:1] == 'D':
                continue
            elif status[:1] == 'M':
                continue
            else:
                print(status)
        msg = f'--> auto commit Proj. {os.path.basename(wc)}'
        print(f'Commit {os.path.basename(wc)}')
        commit(item=wc, msg=msg)
    return


def main():
    while True:
        user_input = input(
            'You want Shutdown (s) or Restart (r) your System? (s/r) or just commit (c): ')
        if user_input in ['R', 'r', 'S', 's', 'C', 'c']:
            break
    svn_func()
    time.sleep(5)
    if user_input in ['s', 'S']:
        os.system('shutdown.exe /s /t 00')
    elif user_input in ['r', 'R']:
        os.system('shutdown.exe /r /t 00')
    elif user_input in ['C', 'c']:
        print('Commiting finished')
        os.system('pause')
        pass


if __name__ == '__main__':
    main()
