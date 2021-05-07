#!/usr/bin/env python3.9

import os

local_nx = r'D:\NX_DMGMORI\NXLocal' # Path for my local NX where i make the changes
server_nx = r'B:\032_Projects_2\NX\NXServer'

while True:
    comment = input('Please enter a comment!:')
    if comment != '':
        break

os.system(f'svn add "{local_nx}" --force')
os.system(r'scn ci B:\032_Projects_2\NX\NXServer\NXcustom\NX1953library\CAMresource\device -m auto commit')
os.system(r'scn ci B:\032_Projects_2\NX\NXServer\NXcustom\NX1953library\CAMresource\tool -m auto commit')
os.system(f'svn ci "{local_nx}" -m "{comment}"')
