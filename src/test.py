import os
import subprocess
import platform

def add(item):
    cmd = ' '.join([f'svn add "{item}" --force'])
    subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    pass

def commit(item, msg):
    cmd = ' '.join([f'svn ci {item} -m "{msg}"'])
    subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    pass

def remove(item, msg=''):
    if msg == '':
        cmd = ' '.join(f'svn rm {item}')
        subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    else:
        cmd = ' '.join([f'svn rm {item} -m "{msg}"'])
        print(subprocess.run(cmd))
    pass

def main():
    if platform.system() == 'Linux':
        path = '/home/christoph/Dokumente/test/trunk'
    elif platform.system() == 'Windows':
        path =r'D:\SVN\V-Projekte'

    for wk in os.listdir(path):
        wk = os.path.join(path, wk)
        cmd = " ".join(['svn st', wk])
        output = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        for status in output.stdout.splitlines():
            print(status)
            if status[:1] == '!':
                remove(item=status[8:])
            elif status[:1] == 'A':
                continue
            elif status[:1] == '?':
                add(status[8:])
            elif status[:1] == 'D':
                continue               
    msg = f'--> auto commit Proj. {os.path.basename(wk)}'
    commit(item=wk, msg=msg)
    return
   
if __name__ == '__main__':
    main()
    