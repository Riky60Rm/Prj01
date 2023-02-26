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
# inputDir = '/media/FreeNas'
inputDir = '/media/1TbF/tmp/Magazine'
# inputDir = '/media/Qnap/Disinformazione/YouTube'

# -----------------------------------------------------------------------------------------
# define the key of sort
# -----------------------------------------------------------------------------------------
def sortkey(elem):
    return elem.split('/')[7]


# -----------------------------------------------------------------------------------------
# define the value of syntax string
# -----------------------------------------------------------------------------------------
def syntax():
    parser = ArgumentParser(prog="ListDirpy", description = """
    ------------------------- it will work on '/media/Rpi3B+Download/Download' directory ----------------------- "
    Program to move the downloaded file which are one per directory to a unique directory. the new directory 
    name has to be contained in the downloaded directory name.
     es : 
       downloaded dir name : Star.Trek.Strange.New.Worlds.S01E05.Buffo.Come.Spock.WEBMux.720P.ITA.ENG.AC3.x264-Prometheus
       new directory name  : Strange 
       the shell will find for all the dir name which contain 'Strange' and move the files contained to the 'Strange' dir""",
                    epilog = 'Text at the bottom of help')

    parser.add_argument("inputDir", help="directory that will be created",type=str)
    parser.add_argument("-h", "--help", help="" )
    args: Namespace = parser.parse_args()

    return None


# r=root, d=directories, f = files
for r, d, f in os.walk(inputDir):
    print ("r value is " , r)
    print("d value is ", d)
    print ("f value is " , f)
    # for file in f:
    #     st = os.stat(os.path.join(r, file))
    #     # print(st[ST_SIZE], file)
    #     # print("{:14,.0f}".format(st[ST_SIZE]), file)
    #     ModTime = time.strftime("%d/%m/%Y %I:%M:%S %p", time.localtime(st[ST_MTIME]))
    #     files.append("{:14,.0f}".format(st[ST_SIZE]) + "  " + ModTime + "  " + os.path.join(r, file))

sys.exit(2)


    # print("------------------ print 'files' content ------------------------")
    # sort the list of file by name
    # lamba split a file name in a list at the "/" delimiter and
    #           then takes the last element of the list
    print("=================== print 'files' content unsorted ========================")
    print (files)

    files.sort(key=lambda x: x.split('/')[-1])
    print("------------------ print 'files' content ------------------------")
    for f in files:
        print(f)

# -----------------------------------------------------------------------------------------
# create the name of file
# -----------------------------------------------------------------------------------------
# Look at another Example
d = datetime.datetime.today()
# print(d.strftime("%d.%m.%Y.%H.%M.%S"))
fName = "/media/1TbF/tmp/ElencoFile." + d.strftime("%Y.%m.%d") + ".txt"

# -----------------------------------------------------------------------------------------
# write the file
# -----------------------------------------------------------------------------------------
file = open(fName, "w")
for f in files:
    file.write(f + "\n")
file.close()

print("    ")
print("-----------------------------------------------------------------------------------")
print(fName, " contains the list of file in ", inputDir)
print("-----------------------------------------------------------------------------------")

sys.exit(22)
