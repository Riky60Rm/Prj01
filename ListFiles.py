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
    return ('Syntax : ' + ShName + ' -i <inputDir> \n' 
            "   where inputDir is the directory we want to list, \n" 
            "   if not specified inputDir it will be used the default \n" 
            "   inputDir, which actually is : " + inputDir + "\n")


# if it is executed as main module and not called
if __name__ == "__main__":
    # Get the arguments from the command-line except the filename
    # argv = sys.argv[1:]
    if len(sys.argv[1:]) == 2:
        try:
            opts, args = getopt.getopt(sys.argv[1:], "i:", ["inputDir="])
        except getopt.GetoptError:
            print(ShName + ' wrong parameters ')
            print(syntax())
            sys.exit(2)
        for opt, arg in opts:
            if opt == '-h':
                print(syntax())
                sys.exit()
            elif opt in ("-i", "--idir"):
                inputDir = arg
                print("List of file contained in : ", inputDir)
    else:
        print("No parameter has been included")
        print(syntax())
        sys.exit()

    # r=root, d=directories, f = files
    for r, d, f in os.walk(inputDir):
        # print ("f value is " , f)
        for file in f:
            st = os.stat(os.path.join(r, file))
            # print(st[ST_SIZE], file)
            # print("{:14,.0f}".format(st[ST_SIZE]), file)
            ModTime = time.strftime("%d/%m/%Y %I:%M:%S %p", time.localtime(st[ST_MTIME]))
            files.append("{:14,.0f}".format(st[ST_SIZE]) + "  " + ModTime + "  " + os.path.join(r, file))

    # sys.exit(2)


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
