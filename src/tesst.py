
import subprocess
import re
import os
import sys
import tempfile
import shutil

# if you change this array you need to change the function that gets the mapping as well 
OWNERS = { 'svnusername': 'firstname.lastname@company.com',
          }


class Revision:
    def __init__(self, number, commiter, timestamp,):
        self._rev = number
        self._commiter = commiter
        self._timestamp = timestamp
        self._message = None

    @property
    def rev(self):
        return self._rev

    @property
    def timestamp(self):
        return self._timestamp

    @property
    def commiter(self):
        return self._commiter

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value):
        self._message = value


def fileSystemPatch(item, svndir):
    rev = item.rev
    cmd = " ".join(['svn update', svndir, '-r', rev])
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output, stderr = p.communicate()
    print (output)
    cmd = " ".join(['svn', 'log', svndir, '-r', 'BASE'])
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output, stderr = p.communicate()
    description = " ".join(output.split('\n')[3:-2])
    item.message = description


def patch(item, svnurl, gitdir):
    rev = item.rev
    cmd = " ".join(['svn log', svnurl, '-c', rev])
    p = subprocess.call(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output, stderr = p.communicate()
    description = " ".join(output.split('\n')[3:-2])

    temp = tempfile.mkstemp()
    cmd = " ".join(['svn', 'diff', svnurl, '-x -w', '-c', rev, '>', temp[1]])
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output, stderr = p.communicate()
    cmd = " ".join(['patch', '-p0', '-E', '-f', '--ignore-whitespace', '<', temp[1]])
    p = subprocess.Popen(cmd, cwd=gitdir, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output, stderr = p.communicate()
    status = p.returncode
    os.unlink(temp[1])
    item.message = description


def generateCommit(item, path):
    cmd = " ".join(['git', 'add', '-A'])
    p = subprocess.Popen(cmd, cwd=path, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output, stderr = p.communicate()
    status = p.returncode
    author = "".join(['--author=', '"', OWNERS[item.commiter].split('@')[0].replace('.', " ").title(), " <", OWNERS[item.commiter], '>"'])
    svndate = "".join(['--date=', '"', item.timestamp.split("(")[1][:-1], " ", item.timestamp.split(" ")[1], " ", item.timestamp.split(" ")[2], '"'])
    cmd = " ".join(['git', 'commit', author, svndate, '-m', '"', item.rev, item.message, '"'])
    p = subprocess.Popen(cmd, cwd=path, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output, stderr = p.communicate()
    print (output)
    status = p.returncode


def getSvnCommits(svnurl, startrev):
    revString = "HEAD:" + startrev
    cmd = " ".join(['svn log', '--stop-on-copy', svnurl, '-r', revString])
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output, stderr = p.communicate()
    status = p.returncode
    revisions = []
    for line in output.split("\n"):
        if re.search(r"^r\d+", line):
            values = [x.strip(' ') for x in line.split('|')]
            newrev = Revision(values[0], values[1], values[2])
            revisions.insert(0, newrev)
    if len(revisions) > 0:
        revisions.pop(0)
    return revisions


def svnCheckout(url, revision, gitpath):
    path = tempfile.mkdtemp()
    cmd = " ".join(['svn', 'checkout', url, '-r', revision, path])
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output, stderr = p.communicate()
    status = p.returncode
    print (output)
    return path


def svnGitMerge(svnurl, latestRevision, gitpath):
    svndir = svnCheckout(svnurl, latestRevision.rev, gitpath)
    cmd = " ".join(['cp', '-prf', gitpath + '/.git', svndir])
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output, stderr = p.communicate()
    print (output)
    status = p.returncode
    with open(svndir + '/.gitignore', 'wb+') as f:
        f.write('.svn\n')

    return svndir


def gitClone(url, branch, path):
    cmd = " ".join(['git', 'clone', '-b', branch, url, path])
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output, stderr = p.communicate()
    status = p.returncode
    cmd = " ".join(['git', 'log', '-1', '--pretty=%s'])
    p = subprocess.Popen(cmd, cwd=path, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output, stderr = p.communicate()
    status = p.returncode
    return output.split('\n')[0].strip().split(" ")[0]


def gitPush(path, branch):
    cmd = " ".join(['git', 'push', '-u', 'origin', branch])
    p = subprocess.Popen(cmd, cwd=path, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output, stderr = p.communicate()
    status = p.returncode
    print ("Push to remote:", output)


def OldMain(args):
    svnurl = args[0]
    giturl = args[1]
    branch = args[2]
    path = tempfile.mkdtemp()
    latestRevision = gitClone(giturl, branch, path)
    if not re.match(r'r\d+', latestRevision):
        print ("Can't find revision id to start from")
        latestRevision = '0'
    revisions = getSvnCommits(svnurl, latestRevision)
    for item in revisions:
        print ("working on rev %s" % item.rev)
        patch(item, svnurl, path)
        generateCommit(item, path)

    gitPush(path, branch)
    print ("Cleaning temp directory")
    shutil.rmtree(path)
    print ("Finished running")
    sys.exit(0)


def main(args):
    svnurl = args[0]
    giturl = args[1]
    branch = args[2]
    gitpath = tempfile.mkdtemp()
    latestRevision = gitClone(giturl, branch, gitpath)
    if not re.match(r'r\d+', latestRevision):
        print ("Cant find revision id to start from")
        latestRevision = '0'
    revisions = getSvnCommits(svnurl, latestRevision)
    if len(revisions) > 0:
        svnpath = svnGitMerge(svnurl, revisions[0], gitpath)

        for item in revisions:
            print ("working on rev %s" % item.rev)
            fileSystemPatch(item, svnpath)
            generateCommit(item, svnpath)

        gitPush(svnpath, branch)
    print ("Cleaning temp directory")
    shutil.rmtree(gitpath)
    if len(revisions) > 0:
          shutil.rmtree(svnpath)
    print ("Finished running")
    sys.exit(0)

if __name__ == "__main__":
    main(sys.argv[1:])