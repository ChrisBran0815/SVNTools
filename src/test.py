from os import popen
import subprocess


def main():
    path = '/home/christoph/Dokumente/test/trunk'
    cmd = " ".join(['svn info --show-item=url', path])
    status = subprocess.Popen(cmd, shell=True)


if __name__ == '__main__':
    main()