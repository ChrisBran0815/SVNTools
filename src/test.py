from os import popen
import subprocess


def main():
    path = '/home/christoph/Dokumente/test/trunk'
    path2 = r'D:\SVN\V-Projekte\VT_20210712-05_Hawle_Armaturenwerke_GmbH'
    cmd = " ".join(['svn info --show-item=url', path2])
    status = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

    for i in status.stdout:
        print(i)
    

if __name__ == '__main__':
    main()