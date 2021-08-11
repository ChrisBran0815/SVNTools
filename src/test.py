import os
import subprocess


def main():
    path = '/home/christoph/Dokumente/test/trunk'
    cmd = " ".join(['svn info --show-item=url', path])
    status = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE ,universal_newlines=True)

    print(status.stdout.splitlines())
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