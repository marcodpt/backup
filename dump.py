#!/usr/bin/python3

import json
import os 
from datetime import datetime

def run(cmd):
    os.system(cmd)

path = os.path.dirname(os.path.realpath(__file__))+'/config.json'

if not os.path.isfile(path):
    print("Error: Unable to locate file <"+path.split('/').pop()+">")
    quit()
    
with open(path) as filePtr:    
    Actions = json.load(filePtr)

def putTime(name):
    iso = str(datetime.now()).replace(" ", "T", 1)
    iso = iso[0:16].replace(':', '_')
    return name.replace('*', iso)

for Action in Actions:
    fullPath = putTime(Action['target'])
    T = fullPath.split('/')
    target = T.pop()
    os.chdir('/'.join(T))
    print ("***** Copying: "+target+" *****")
    run('scp '+Action['source']+' '+target)
    ext = ''
    if 'compress' in Action and Action['compress']:
        ext = '.tar.gz'
        print ("***** Compressing: "+target+ext+" *****")
        run('tar -zcf '+target+ext+' '+target)
        run('rm '+target)
    if 'limit' in Action and Action['limit'] > 0:
        files = os.popen(
            "ls "+Action['target']+ext+' 2>/dev/null'
        ).read().split("\n")
        files.pop()
        i = 0
        while i < len(files) - Action['limit']:
            print ("***** Remove: "+files[i]+" *****")
            run('rm '+files[i])
            i = i + 1
