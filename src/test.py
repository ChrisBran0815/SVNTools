import os
import subprocess
import platform


def main():
    if platform.system() == 'Linux':
        path = '/home/christoph/Dokumente/test/trunk'
    elif platform.system() == 'Windows':
        path =r'D:\SVN\V-Projekte'

    for wk in os.listdir(path):
        wk = os.path.join(path, f'"{wk}"')
        cmd = " ".join(['svn st', wk])
        output = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        for status in output.stdout.splitlines():
            if status[:1] == '!':
                cmd = ' '.join(['svn rm', f'"{status[8:]}"'])
                print(subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True))
                print(status[8:])
            #status = status[1:]
            
            print(status)

   # !M      D:\SVN\V-Projekte\VT_20210816-13_Warema\02_CAM\01_Setup\519378_ke031610051_165-setup_1  Copy.prt    
   # A       D:\SVN\V-Projekte\VT_20210816-13_Warema\02_CAM\01_Setup\519378_ke031610051_165-setup_1.prt
    return
    i = 0
    while i == 0:
        print('HELLO')
        cmd = " ".join(['svn status', path])
        list = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE ,universal_newlines=True)
        print(list.stdout.splitlines())
        for content in list.stdout.splitlines():
            if "!" in content:
                print('yes')
                cmd=' '.join(['svn rm', content[1:]])
                test = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE ,universal_newlines=True)
                print(test.stdout.splitlines())
        i += 1
    
if __name__ == '__main__':
    main()
    