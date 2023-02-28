"""
List files on a specific device/directory
"""

# cd ~/PycharmProjects/Proj1/venv/bin
# !/usr/bin/python3

import datetime
import time
import os
import sys
import getopt
from stat import *  # ST_SIZE
from typing import List
from argparse import ArgumentParser , Namespace

ShName = os.path.basename(__file__)

# print ("Program name " + ShName)

files = []  # type: List[str]
# WorkDir = '/media/Rpi3B+Download/Download'
# WorkDir = '/media/riky60/12Tb/tmp/pippo'
WorkDir = '/media/ramdsk/pippo'
# WorkDir = " "
inputDir = ""
inputDirCreated : bool = False

# -----------------------------------------------------------------------------------------
# define the key of sort
# -----------------------------------------------------------------------------------------
def createDir(inputDir):
    global inputDirCreated , WorkDir
    cmd = "mkdir " + '"' + WorkDir + '/' + inputDir + '"'
    rslt = os.system(cmd)
    # rslt = 0
    if rslt == 0 :
        print("The directory " + WorkDir + '/' + inputDir + "has been created")
        print(" ")
    elif rslt == 256 :
        print("Error the directory " + WorkDir + '/' + inputDir + "already exists")
        exit(12)
    else :
        print("Error creating the directory " + WorkDir + '/' + inputDir + "return code is ", rslt)
        exit(12)
    inputDirCreated = True

# -----------------------------------------------------------------------------------------
# define the value of syntax string
# -----------------------------------------------------------------------------------------
def syntax():
    global inputDir
    parser = ArgumentParser(prog="ListDirpy", description = """
    ------------------------- it will work on '/media/Rpi3B+Download/Download' directory ----------------------- "
    Program to move the downloaded file which are one per directory to a unique directory. the new directory 
    name has to be contained in the downloaded directory name.
     es : 
       downloaded dir name : Star.Trek.Strange.New.Worlds.S01E05.Buffo.Come.Spock.WEBMux.720P.ITA.ENG.AC3.x264-Prometheus
       new directory name  : Strange 
       the shell will find for all the dir name which contain 'Strange' and move the files contained to the 'Strange' dir""",
                    epilog = 'Text at the bottom of help')

    parser.add_argument("inputDir", help="directory that will be created and where to move the files",type=str)
    #parser.add_argument("-h", "--help", help="help" )
    args: Namespace = parser.parse_args()
    print("inputDir = ",args.inputDir)
    inputDir = args.inputDir

    return None


syntax()
createDir(inputDir)
# r=root, d=directories, f = files
for r, d, f in os.walk(WorkDir):
    #print("r =", r, " ", type(r))
    #print("d =", d, " ", type(d))
    #print("f =", f, " ", type(f))
    if r.find(inputDir) == -1 :
        continue
    elif len(f) == 0 :
        continue
    else :
        cmd = "mv " + '"' + r + '/' + f[0] + '" ' + WorkDir + '/' + inputDir
        rslt = os.system(cmd)
        if rslt == 0:
            print("file ", f[0] , " moved")
        else :
            print(cmd)
            print("ERROR moving file " , f)
        print(" ")
        # print(cmd)
        print("-----------------------------------------------------------------------------")

# cp -rv /media/riky60/12Tb/tmp/pippo /media/ramdsk


sys.exit(0)
