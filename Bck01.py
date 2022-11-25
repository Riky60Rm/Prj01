"""
implementation of a program to manage user choices

"""
# cp /home/riky60/PycharmProjects/Prj01/Menu01.py  /home/riky60/Shell/Python

import csv
import datetime
import os
import re
import sys
import platform
import colorama
from colorama import Fore, Back, Style
import logging
colorama.init()


RELEASE_DATA = {}     #dictionary
arch = platform.architecture()

#print(type(RELEASE_DATA))
len_delimiter = 100
script_name = os.path.basename(__file__)
logging.basicConfig(filename='Bck01.log', encoding='utf-8', level=logging.INFO)
# logging.debug('This message should go to the log file')
# logging.info('So should this')
# logging.warning('And this, too')
# logging.error('And non-ASCII stuff, too, like Øresund and Malmö')

Bck = 1
BckPath = "/media/riky60/12Tb/Bck/"

d = datetime.datetime.today()
BckDate = d.strftime("%Y.%m.%d")

#=======================================================================================
def set_Backup_dir() :
    global BckPath
    print("Select backup directory")
    print("  1 - /media/riky60/12Tb/Bck")
    print("  2 - /media/Qnap")
    print("  3 - /media/ramdsk")
    Bck = int(input("Select "))
    if Bck == 1:
        BckPath = "/media/riky60/12Tb/Bck/"
    elif Bck == 2:
        BckPath = "/media/Qnap/"
    else:
        BckPath = "/media/ramdsk/"


#=======================================================================================
def set_windows_size() :
    # set the windows size to 100x32
    os.system("printf '\e[8;32;100t'")

    # Move the window to the top/left corner of the display:
    # os.system("printf '\e[3;0;0t'")

    # Minimize the window
    # os.system("printf '\e[2t'")


# =======================================================================================
def screen_clear():
    # for mac and linux(here, os.name is 'posix')
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        # for windows platfrom
        _ = os.system('cls')


# =======================================================================================
def get_system_info () :
    # print("=============================================================================")
    # logger = logging.getLogger(__name__)
    # logging.info('Entry into')
    # print("=============================================================================")
    with open('/etc/os-release') as f:
    # with open('/home/riky60/PycharmProjects/Prj01/Data/os-release') as f:
        reader = csv.reader(f, delimiter="=")
        for row in reader:
            # print(row)
            if row:
                RELEASE_DATA[row[0]] = row[1]
    #
    #

# =======================================================================================
def get_mount_list () :
    print('list of NFS mounted')
    void = input("Press a key to continue")
    # rslt = os.system(cmd)
    myCmd = os.popen('mount | grep nfs[^d]').read()
    if myCmd.count("nfs") > 0:
        if myCmd.count("nfs") == 1:
            print(Fore.GREEN + Style.BRIGHT + myCmd[:(myCmd.find("nfs") + 4)] + Style.RESET_ALL)
            # print("llllllll")
        else:
            loop = True
            myCmdList = myCmd.split("\n")
            for Ls in myCmdList :
                if len(Ls) > 0 :
                    #print (Ls)
                    print(Fore.GREEN + Style.BRIGHT + Ls[:(Ls.find("nfs") + 4)] + Style.RESET_ALL)

            #print("more than one 'NFS drive' active")
    else:
        print(Fore.RED + Style.BRIGHT + "No NFS mount active" + Style.RESET_ALL + Fore.RESET)

    # myCmd = os.popen('df -h | grep ramdsk').read()
    myCmd = os.popen('df -h').read()
    myCmdList = myCmd.split("\n")
    title = myCmdList[0]
    for ls in myCmdList :
        if ls.find("ramdsk") > 0 :
            print(title)
            print(ls)
    # print("------------------")
    # print(myCmd)

# =======================================================================================

def InternetConfiguration() :

    target = BckPath + "InternetConfiguration." + BckDate + ".txt"
    cmd = "cp /media/1TbF/320Gb/TRANFILE/InternetConfiguration.txt " + target
    os.system(cmd)
    logging.info('Created ' + target)

    target = BckPath + "OperationsSetup." + BckDate
    cmd = "cp /home/riky60/Desktop/OperationsSetup " + target
    os.system(cmd)
    logging.info('Created ' + target)

    target = BckPath + "TorrentConfiguration." + BckDate + ".txt"
    cmd = "cp /media/1TbF/320Gb/TRANFILE/TorrentConfiguration.txt " + target
    os.system(cmd)
    logging.info('Created ' + target)

# =======================================================================================

def Doc() :

    DirToSave = "/media/1TbF/300Gb/DOC"
    target = BckPath + "DOC." + BckDate + ".tar "
    cmd = "tar -cvf " + target + DirToSave
    os.system(cmd)
    logging.info('Created ' + target)
    # cmd = "7z a " + BckPath + "DOC." + BckDate + ".tar.7z " + BckPath +"DOC." +BckDate + ".tar"
    # os.system(cmd)

# =======================================================================================

def HelpTricks() :

    DirToSave = "\"/media/1TbF/320Gb/Help & Tricks\""
    target = '"' + BckPath + "Help&Tricks." + BckDate + ".tar" + '"' + " "
    cmd = "tar -cvf " + target  + DirToSave
    # print(cmd)
    os.system(cmd)
    logging.info('Created ' + target)

# =======================================================================================

def BiosDrivers():
    DirToSave = "\"/media/1TbF/320Gb/Bios&Drivers\""
    target = '"' + BckPath + "Bios&Drivers." + BckDate + ".tar" + '"' + " "
    cmd = "tar -cvf " + target + DirToSave
    # print(cmd)
    os.system(cmd)
    logging.info('Created ' + target)


 # =======================================================================================

def LavoriConsulenza():
    DirToSave = "\"/media/1TbF/320Gb/Lavori Consulenza\""
    target = BckPath + "LavoriConsulenza." + BckDate + ".tar "
    cmd = "tar -cvf " + target + DirToSave
    # print(cmd)
    os.system(cmd)
    logging.info('Created ' + target)

# =======================================================================================

def Varie():
    DirToSave = "/media/1TbF/320Gb/Varie"
    target = BckPath + "Varie." + BckDate + ".tar "
    cmd = "tar -cvf " + target + DirToSave
    # print(cmd)
    os.system(cmd)
    logging.info('Created ' + target)

# =======================================================================================

def Disinformazione():
    print( Fore.LIGHTYELLOW_EX + "/media/1TbF/320Gb/Disinformazione/YouTube will be excluded from TAR" + Fore.RESET)
    input("Press  key to continue")
    DirToSave = "/media/1TbF/320Gb/Disinformazione"
    target = BckPath + "Disinformazione." + BckDate + ".tar " + "--exclude=\"/media/1TbF/320Gb/Disinformazione/YouTube\" "
    cmd = "tar -cvf " + target + DirToSave
    # print(cmd)
    os.system(cmd)
    logging.info('Created ' + target)

# =======================================================================================

def Pgm():
    DirToSave = "/media/1TbF/320Gb/Pgm"
    target = BckPath + "Pgm." + BckDate + ".tar "
    cmd = "tar -cvf " + target + DirToSave
    # print(cmd)
    os.system(cmd)
    logging.info('Created ' + target)

# =======================================================================================

def riky60():
    DirToSave = "/home/riky60"
    target = BckPath + "riky60." + BckDate + ".tar "
    cmd = "tar -cvf " + target + DirToSave
    # print(cmd)
    os.system(cmd)
    logging.info('Created ' + target)
# =======================================================================================

def user01():
    DirToSave = "/home/user01"
    target = BckPath + "user01." + BckDate + ".tar "
    cmd = "echo \"riky60\" | sudo -S tar -cvf " + target + DirToSave
    # print(cmd)
    os.system(cmd)
    logging.info('Created ' + target)
    cmd = "echo \"riky60\" | sudo -S chown riky60 " + target
    # print(cmd)
    os.system(cmd)
    logging.info('Changed owner of ' + target)

    DirToSave = "/media/1TbF/User01"
    target = BckPath + "user01.1TbF." + BckDate + ".tar "
    cmd = "echo \"riky60\" | sudo -S tar -cvf " + target + DirToSave
    # print(cmd)
    os.system(cmd)
    logging.info('Created ' + target)
    cmd = "echo \"riky60\" | sudo -S chown riky60 " + target
    # print(cmd)
    os.system(cmd)
    logging.info('Changed owner of ' + target)



# =======================================================================================


def get_user_input() :
    choice = ""
    global mn_lev
    device = "1>/dev/null 2>/dev/null"

    while True:
        choice = input("choose a menu item : ")
        # print("script_name = " + script_name)
        # print("ascii value of "+ choice + " is " + str(ord(choice)))
        result = re.findall('[0-9]+', choice)
        # print(result)
        if (choice == 'x' ) or (choice == 'X'):
            if mn_lev == 1 :
                exit(0)
            elif mn_lev == 5 :
                mn_lev = 1
            break
        elif (choice == '' ) :
            break
        else :
            if len(result) > 0 and ((int(choice) > 0) or (int(choice) < 99)):
                int_choice = int(choice)

                if int_choice == 1 :
                    mn_lev = 1
                    InternetConfiguration()
                # ====================================================================
                if int_choice == 2 :
                    mn_lev = 1
                    Doc()

                # ====================================================================
                if int_choice == 3 :
                    mn_lev = 1
                    HelpTricks()

                # ====================================================================
                if int_choice == 4 :
                    mn_lev = 1
                    BiosDrivers()

                # ====================================================================
                if int_choice == 5 :
                    mn_lev = 1
                    LavoriConsulenza()

                # ====================================================================
                if int_choice == 6 :
                    mn_lev = 1
                    Varie()

                # ====================================================================
                if int_choice == 7 :
                    mn_lev = 1
                    Disinformazione()

                # ====================================================================
                if int_choice == 8 :
                    mn_lev = 1
                    Pgm()

                # ====================================================================
                if int_choice == 9 :
                    mn_lev = 1
                    riky60()

                # ====================================================================s
                if int_choice == 10 :
                    mn_lev = 1
                    user01()

                # ====================================================================
                if int_choice == 17 :
                    mn_lev = 1
                    print('choose to backup all , it will take considerable amount of time')
                    print('are you sure you want to continue')
                    void = input("Press a key to continue or Ctrl+C to abort")
                    InternetConfiguration()
                    Doc()
                    HelpTricks()
                    BiosDrivers()
                    LavoriConsulenza()
                    Varie()
                    Disinformazione()
                    Pgm()
                    riky60()
                    user01()

                # ====================================================================
                if int_choice == 20 :
                    mn_lev = 1
                    set_Backup_dir()



                # ====================================================================
                if int_choice == 50 :
                    # mn_lev = 5
                      mn_lev = 1
                elif int_choice == 51 :
                    if mn_lev == 5 :
                        print('Mount Raspberry Pi  on /media/Rpi3B+Download')
                        void = input("Press a key to continue")
                        cmd = "echo \"riky60\" | sudo -S mount -vvvv -o nfsvers=4 192.168.1.164:/ /media/Rpi3B+Download 1>/dev/null 2>/dev/null"
                        os.system(cmd)
                        void = input("Press a key to continue")
                        # continue

                elif int_choice == 52 :
                    if mn_lev == 5 :
                        print('UMount Raspberry Pi  on /media/Rpi3B+Download')
                        void = input("Press a key to continue")
                        cmd = "echo \"riky60\" | sudo -S umount /media/Rpi3B+Download 1>/dev/null 2>/dev/null"
                        os.system(cmd)
                        void = input("Press a key to continue")
                        #continue

                elif int_choice == 53 :
                    if mn_lev == 5 :
                        print('Mount Qnap on /media/Qnap')
                        void = input("Press a key to continue")
                        cmd = "echo \"riky60\" | sudo -S mount 192.168.1.202:/Qnap /media/Qnap 1>/dev/null 2>/dev/null"
                        os.system(cmd)
                        void = input("Press a key to continue")
                        #continue

                elif int_choice == 54:
                    if mn_lev == 5:
                        print('UMount Qnap on /media/Qnap')
                        void = input("Press a key to continue")
                        cmd = "echo \"riky60\" | sudo -S umount /media/Qnap"
                        os.system(cmd)
                        void = input("Press a key to continue")
                        #continue

                elif int_choice == 55 :
                    if mn_lev == 5 :
                        print('Mount Qnap on /media/Qnap2')
                        void = input("Press a key to continue")
                        cmd = "echo \"riky60\" | sudo -S mount 192.168.1.202:/Qnap /media/Qnap2"
                        os.system(cmd)
                        void = input("Press a key to continue")
                        #continue
                elif int_choice == 56:
                    if mn_lev == 5:
                        print('UMount Qnap2 on /media/Qnap2')
                        void = input("Press a key to continue")
                        cmd = "echo \"riky60\" | sudo -S umount /media/Qnap2"
                        os.system(cmd)
                        void = input("Press a key to continue")
                        #continue

                elif int_choice == 57 :
                    if mn_lev == 5 :
                        print('Mount FreeNas /media/FreeNas')
                        void = input("Press a key to continue")
                        cmd = "echo \"riky60\" | sudo -S mount 192.168.1.151:/mnt/FreeNas12Tb /media/FreeNas"
                        os.system(cmd)
                        void = input("Press a key to continue")
                        #continue

                elif int_choice == 58:
                    if mn_lev == 5:
                        print('UMount FreeNas on /media/FreeNas')
                        void = input("Press a key to continue")
                        cmd = "echo \"riky60\" | sudo -S umount /media/FreeNas"
                        os.system(cmd)
                        void = input("Press a key to continue")
                        #continue

                elif int_choice == 59 :
                    if mn_lev == 5 :
                        print('Mount nfs-low /media/nfs-low')
                        void = input("Press a key to continue")
                        cmd = "echo \"riky60\" | sudo -S mount 192.168.1.144:/media/700Gb /media/nfs-low"
                        os.system(cmd)
                        void = input("Press a key to continue")
                        #continue

                elif int_choice == 60:
                    if mn_lev == 5:
                        print('UMount nfs-low on /media/nfs-low')
                        void = input("Press a key to continue")
                        cmd = "echo \"riky60\" | sudo -S umount /media/nfs-low"
                        os.system(cmd)
                        void = input("Press a key to continue")
                        #continue

                elif int_choice == 61:
                    if mn_lev == 5:
                        print('Mount Phenom 1TbF on /media/1TbFPhe')
                        void = input("Press a key to continue")
                        cmd = "echo \"riky60\" | sudo -S mount 192.168.1.183:/media/1TbF /media/1TbFPhe"
                        os.system(cmd)
                        void = input("Press a key to continue")
                        # continue

                elif int_choice == 62:
                    if mn_lev == 5:
                        print('UMount Phenom 1TbF on /media/1TbFPhe')
                        void = input("Press a key to continue")
                        cmd = "echo \"riky60\" | sudo -S umount /media/1TbFPhe"
                        os.system(cmd)
                        void = input("Press a key to continue")
                        # continue

                elif int_choice == 63:
                    if mn_lev == 5:
                        print('Mount Phenom 2TbF on /media/2TbFb')
                        void = input("Press a key to continue")
                        cmd = "echo \"riky60\" | sudo -S mount 192.168.1.183:/media/2TbFb /media/2TbFb"
                        os.system(cmd)
                        void = input("Press a key to continue")
                        # continue

                elif int_choice == 64:
                    if mn_lev == 5:
                        print('UMount Phenom 2TbF on /media/2TbFb')
                        void = input("Press a key to continue")
                        cmd = "echo \"riky60\" | sudo -S umount /media/2TbFb"
                        os.system(cmd)
                        void = input("Press a key to continue")
                        # continue

                elif int_choice == 65:
                    if mn_lev == 5:
                        print('Mount Phenom 8TbF on /media/8TbF')
                        void = input("Press a key to continue")
                        cmd = "echo \"riky60\" | sudo -S mount 192.168.1.183:/media/8TbF /media/8TbF"
                        os.system(cmd)
                        void = input("Press a key to continue")
                        # continue

                elif int_choice == 66:
                    if mn_lev == 5:
                        print('UMount Phenom 8TbF on /media/8TbF')
                        void = input("Press a key to continue")
                        cmd = "echo \"riky60\" | sudo -S umount /media/8TbF"
                        os.system(cmd)
                        void = input("Press a key to continue")
                        # continue

                elif int_choice == 67 :
                    if mn_lev == 5 :
                        print('Create a ram disk')
                        size = input("type the size of disk you wish to create (1024m = 1Gb) ")
                        # void = input("Press a key to continue")
                        cmd = "echo \"riky60\" | sudo -S mount -t tmpfs -o size="+ size +" new_ram_disk /media/ramdsk 1>/dev/null 2>/dev/null"
                        # print(cmd)
                        rslt = os.system(cmd)
                        void = input("Press a key to continue")
                        # continue

                elif int_choice == 68:
                    if mn_lev == 5:
                        print('UMount /media/ramdsk')
                        void = input("Press a key to continue")
                        cmd = "echo \"riky60\" | sudo -S umount /media/ramdsk 1>/dev/null 2>/dev/null"
                        os.system(cmd)
                        void = input("Press a key to continue")
                        # continue

                elif int_choice == 69 :
                    if mn_lev == 5 :
                        get_mount_list ()
                        void = input("Press a key to continue")
                    break

                else :
                    mn_lev = 1
                break
            else :
                continue


# =======================================================================================


def display_title_bar() :
    curr_time = datetime.datetime.now()
    screen_clear()
    title1 = Fore.LIGHTYELLOW_EX + "=" * len_delimiter + Style.RESET_ALL
    release = Fore.RED + RELEASE_DATA['NAME'] + ' ' + RELEASE_DATA['VERSION'] + Style.RESET_ALL
    name_len = len(RELEASE_DATA['UBUNTU_CODENAME'])
    title2 = str(curr_time)[: 19] + " " * 19 + release + " " * (20 - name_len) \
            + "Ubuntu code name >" + Fore.LIGHTGREEN_EX + RELEASE_DATA['UBUNTU_CODENAME'] + \
             Style.RESET_ALL + "<"
    str_scrname = "script name " + script_name
    num = 40 - len(str_scrname)
    str_scrname = "script name " + Fore.RED + script_name + Fore.RESET
    num1 = 39 - len(" Archit : ") - len(arch[0])
    archit = " " * (num1) + " Archit : " + Fore.LIGHTGREEN_EX + arch[0] + Fore.RESET
    title3 =   str_scrname + " " * (num) + " Menu for backup     " +  archit
    title4 = "saving to " + BckPath

    title5 = title1
    print(title1)
    print(title2)
    print(title3)
    print(title4)
    print(title5)
# =======================================================================================
def display_menu01() :
    display_title_bar()
    row01 = ("01) Backup InternetConfiguration               | 02) Backup /media/1TbF/300Gb/DOC           " ,
             "03) Backup /media/1TbF/320Gb/Help & Tricks     | 04) Backup /media/1TbF/320Gb/Bios&Drivers  " ,
             "05) Backup /media/1TbF/320Gb/Lavori Consulenza | 06) Backup /media/1TbF/320Gb/Varie         " ,
             "07) Backup /media/1TbF/320Gb/Disinformazione   | 08) Backup /media/1TbF/320Gb/Pgm           " ,
             "09) Backup /home/riky60                        | 10) Backup /home/user01 & /media/1TbF/User01 ",
             "11)                                            | 12)                                        " ,
             "13)                                            | 14)                                        " ,
             "15)                                            | 16)                                        " ,
             "17) Backup all                                 | 18)                                        " ,
             "19)                                            | 20) Set Backup directory                   " ,
             "21)                                            | 50)                                        " ,
             "                                               |  x) Exit                                   " )

    for row in row01 :
        print(row)
# =======================================================================================

def display_menu50() :
    display_title_bar()
    row50 = ("51) mount /media/Rpi3B+Download                | 52) umount /media/Rpi3B+Download " ,
             "53) mount /media/Qnap                          | 54) umount /media/Qnap           " ,
             "55) mount /media/Qnap2                         | 56) umount /media/Qnap2          " ,
             "57) mount /media/FreeNas                       | 58) umount /media/FreeNas        " ,
             "59) mount /media/nfs-low                       | 60) umount /media/nfs-low        " ,
             "61) mount /media/1TbFPhe                       | 62) umount /media/1TbFPhe        " ,
             "63) mount /media/2TbFb                         | 64) umount /media/2TbFb          " ,
             "65) mount /media/8TbF                          | 66) umount /media/8TbF           ",
             "67) mount ram disk                             | 68) umount ram disk              " ,
             "69) list NFS mounted                           | 70)                              " ,
             "                                               |  x) Go back                         " )

    for row in row50 :
        print(row)

# =======================================================================================


set_windows_size ()
get_system_info ()

logging.info('==============================================================================')
logging.info('      Backup done on ' + BckDate + " on this path " + BckPath)
logging.info('==============================================================================')
mn_lev = 1
while True :
    if mn_lev == 1 :
        display_menu01()
    elif mn_lev == 5 :
        display_menu50()
    get_user_input()


