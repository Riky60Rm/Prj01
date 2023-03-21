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

os.environ['TERM'] = "linux" # visible in this process + all children
RELEASE_DATA = {}     #dictionary
arch = platform.architecture()
# item and row to hilight
hitem = 1
rowtem = 1

#print(type(RELEASE_DATA))
len_delimiter = 100
script_name = os.path.basename(__file__)
#logging.basicConfig(filename='Menu01.log', encoding='utf-8', level=logging.INFO)
# logging.debug('This message should go to the log file')
# logging.info('So should this')
# logging.warning('And this, too')
# logging.error('And non-ASCII stuff, too, like Øresund and Malmö')

#=======================================================================================
menu01 = {
    1: "Ebay Delivery address", 2: "Cartoleria Cigola", 3: "NFS", 4: "Find duplicate files with fdupes",
    5: "Get media file info", 6: "", 7: "Commands menu", 8: "", 9: "", 10: "",
    11: "", 12: "", 13: "", 14: "", 15: "", 16: "",
    17: "", 18: "", 19: "", 20: "", 21: "", 50: "Mount NFS disks"
}

menu30 = {
    31: "restart NFS" ,
    32: "show NFS status ",
    33: "", 34: "", 35: "", 36: "", 37: "",
    38: "", 39: "", 40: ""
}

menu50 = {
    51: "mount /media/Rpi3B+Download", 52: "umount /media/Rpi3B+Download" ,
    53: "mount /media/Qnap" ,          54: "umount /media/Qnap" ,
    55: "mount /media/Qnap2" ,         56: "umount /media/Qnap2" ,
    57: "mount /media/FreeNas" ,       58: "umount /media/FreeNas" ,
    59: "mount /media/nfs-low" ,       60: "umount /media/nfs-low" ,
    61: "mount media/Phenom" ,         62: "umount /media/Phenom" ,
    63: "" ,                           64: "" ,
    65: "" ,                           66: "" ,
    67: "mount ram disk " ,            68: "umount ram disk" ,
    69: "list NFS mounted"
}
menu70 = {
    71: "Check the last reboot time", 72: "Example of DD copy" ,
    73: "" ,         74: "" ,
    75: "" ,         76: "" ,
    77: "" ,       78: "" ,
    79: "" ,
}


#=======================================================================================

def print_menu(mnu):

    sprtr = chr(124)  # separator char
    hlf_scr = 40      # half screen value
    if mnu == 1 :     # menu level
        menu_options = menu01
    elif mnu == 3 :
        menu_options = menu30
    elif mnu == 5:
        menu_options = menu50
    elif mnu == 7:
        menu_options = menu70
    else :
        print("\n\n")
        print("print_menu function menu level " + str(mnu) + " not found")
        aa = input("Press a key to exit")

    display_title_bar()
    # display the menu dictionary
    for key in menu_options.keys():

        if key < 10 :
            skey = '0' + str(key)
        else :
            skey = str(key)

        # pad the menu line to half screen length
        mnu_len = menu_options[key].__len__()
        if mnu_len < hlf_scr :
            mnu_opt = menu_options[key] + ' ' * (hlf_scr - mnu_len)
        else :
            mnu_opt = menu_options[key][0:hlf_scr]

        #  render one odd and one even menu on the same line
        if key % 2 == 0 :
            two_line = True
            print(Fore.GREEN + skey  + ') ' + Fore.RESET + mnu_opt)
        else :
            two_line = False
            print(Fore.GREEN + skey  + ') ' + Fore.RESET + mnu_opt,end=" " + Fore.LIGHTYELLOW_EX + sprtr + Fore.RESET + " ")

    # last line is always the x option
    if mnu == 1:
        if two_line :
            sexit = ' ' * hlf_scr + "     " + sprtr + Fore.GREEN + "  x) " + Fore.RESET + "Exit "
        else :
            sexit =  Fore.GREEN + " x) " + Fore.RESET + "Exit "
    else :
        if two_line :
            sexit = ' ' * hlf_scr + "     " + sprtr + Fore.GREEN + "  x) " + Fore.RESET + "Go back "
        else :
            sexit =  Fore.GREEN + " x) " + Fore.RESET + "Go back "
    print(sexit)
    print(" ")

#=======================================================================================
def mediainfo() :
    import tkinter as tk
    from tkinter import filedialog
    root = tk.Tk()
    root.withdraw()  # hide the root window
    # show the file chooser dialog and get the selected file
    file_path = filedialog.askopenfilename()
    # print the selected file path
    #print(file_path)
    #print("Get multimedia file info")
    #print("  ")
    #fileinfo = input("Please type the file name with full path ")
    cmd = "mediainfo " + '"' + file_path + '"'
    #print(cmd)
    os.system(cmd)
    void = input("Press a key to continue")

#=======================================================================================
def fdupes() :
    # search for duplicates of files
    print("Search duplicates files with fdupes (comparing MD5 signature of files )")
    print("  ")
    dirToCheck = input("Please type the directory to control (full Path) ")
    if dirToCheck :
        tmpan = input("for the directory given follow subdirectories encountered within ? (y/N) ")
        param = ""
        if tmpan == "y" :
            param = "-r"
        tmpan = input("preserve the first file in each set of duplicates and delete the rest? (y/N) ")
        if tmpan == "y" :
            param = param + "dN"
        result = input("Would you like to create a file with the result ? (full path+name), Enter will not create a file ")
        if result :
            cmd = "fdupes " + param + " " + dirToCheck + " >" + result
        else :
            cmd = "fdupes "+ param + " " + dirToCheck
        os.system(cmd)
        #print(cmd)
        void = input("Press a key to continue")

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
        reader = csv.reader(f, delimiter="=")
        for row in reader:
            # print(row)
            if row:
                RELEASE_DATA[row[0]] = row[1]
    #
    #

# =======================================================================================
def get_mount_list () :
    print(" ")
    print('list of NFS mounted')
    #void = input("Press a key to continue")
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
            print(" ")
            print(title,Fore.GREEN + Style.BRIGHT)
            print(ls,Style.RESET_ALL + Fore.RESET)
    # print("------------------")
    # print(myCmd)


# =======================================================================================

def get_user_input() :
    choice = ""
    global mn_lev
    device = "1>/dev/null 2>/dev/null"

    while True:
        choice = input("choose a menu item : ")
        choice = choice.strip()   # remove leading or trailing spaces
        # print("script_name = " + script_name)
        # print("ascii value of "+ choice + " is " + str(ord(choice)))
        result = re.findall('[0-9]+', choice)
        # print(result)
        if (choice == 'x' ) or (choice == 'X'):
            if mn_lev == 1 :
                sys.exit(0)
            elif mn_lev == 3 :
                mn_lev = 1
            elif mn_lev == 5 :
                mn_lev = 1
            elif mn_lev == 7 :
                mn_lev = 1
            break
        elif (choice == '' ) :
            break
        else :
            if len(result) > 0 and ((int(choice) > 0) or (int(choice) < 99)):
                int_choice = int(choice)

                if int_choice == 1 :
                    if mn_lev == 1 :
                        cmd = "xed /media/1TbF/320Gb/Varie/Ebay/Indirizzo.txt &"
                        os.system(cmd)
                # ====================================================================
                if int_choice == 2 :
                    if mn_lev == 1 :
                        cmd = "xed /media/1TbF/320Gb/Varie/Roberto/CartoleriaCigola.txt &"
                        os.system(cmd)

                # ====================================================================
                if int_choice == 3 :
                    mn_lev = 3
                    break
                # ====================================================================
                if int_choice == 4 :
                    if mn_lev == 1 :
                        fdupes()
                    break
                # ====================================================================
                if int_choice == 5 :
                    if mn_lev == 1 :
                        mediainfo()
                    break
                # ====================================================================
                if int_choice == 7 :
                    mn_lev = 7
                    break
                # ====================================================================
                elif int_choice == 31 :
                    if mn_lev == 3 :
                        print('Restart NFS')
                        void = input("Press a key to continue")
                        cmd = "echo \"riky60\" | sudo -S systemctl restart nfs-kernel-server"
                        os.system(cmd)
                        void = input("Press a key to continue")
                        break
                # ====================================================================
                elif int_choice == 32 :
                    if mn_lev == 3 :
                        print('Show NFS status')
                        void = input("Press a key to continue")
                        cmd = "echo \"riky60\" | sudo -S systemctl status nfs-kernel-server.service"
                        os.system(cmd)
                        void = input("Press a key to continue")
                        break
                # ====================================================================
                if int_choice == 50 :
                    mn_lev = 5
                    break
                # ====================================================================
                elif int_choice == 51 :
                    if mn_lev == 5 :
                        print('Mount Raspberry Pi  on /media/Rpi3B+Download')
                        void = input("Press a key to continue")
                        # cmd = "echo \"riky60\" | sudo -S mount -vvvv -o nfsvers=4 192.168.1.164:/ /media/Rpi3B+Download 1>/dev/null 2>/dev/null"
                        cmd = "echo \"riky60\" | sudo -S mount -vvvv -o nfsvers=4 192.168.1.155:/ /media/Rpi3B+Download 1>/dev/null 2>/dev/null"
                        os.system(cmd)
                        void = input("Press a key to continue")
                        break

                elif int_choice == 52 :
                    if mn_lev == 5 :
                        print('UMount Raspberry Pi  on /media/Rpi3B+Download')
                        void = input("Press a key to continue")
                        cmd = "echo \"riky60\" | sudo -S umount /media/Rpi3B+Download 1>/dev/null 2>/dev/null"
                        os.system(cmd)
                        void = input("Press a key to continue")
                        break

                elif int_choice == 53 :
                    if mn_lev == 5 :
                        print('Mount Qnap on /media/Qnap')
                        void = input("Press a key to continue")
                        cmd = "echo \"riky60\" | sudo -S mount 192.168.1.202:/Qnap /media/Qnap 1>/dev/null 2>/dev/null"
                        os.system(cmd)
                        void = input("Press a key to continue")
                        break

                elif int_choice == 54:
                    if mn_lev == 5:
                        print('UMount Qnap on /media/Qnap')
                        void = input("Press a key to continue")
                        cmd = "echo \"riky60\" | sudo -S umount /media/Qnap"
                        os.system(cmd)
                        void = input("Press a key to continue")
                        break

                elif int_choice == 55 :
                    if mn_lev == 5 :
                        print('Mount Qnap on /media/Qnap2')
                        void = input("Press a key to continue")
                        cmd = "echo \"riky60\" | sudo -S mount 192.168.1.202:/Qnap2 /media/Qnap2"
                        os.system(cmd)
                        void = input("Press a key to continue")
                        break

                elif int_choice == 56:
                    if mn_lev == 5:
                        print('UMount Qnap2 on /media/Qnap2')
                        void = input("Press a key to continue")
                        cmd = "echo \"riky60\" | sudo -S umount /media/Qnap2"
                        os.system(cmd)
                        void = input("Press a key to continue")
                        break

                elif int_choice == 57 :
                    if mn_lev == 5 :
                        print('Mount FreeNas /media/FreeNas')
                        void = input("Press a key to continue")
                        cmd = "echo \"riky60\" | sudo -S mount 192.168.1.151:/mnt/FreeNas12Tb /media/FreeNas"
                        os.system(cmd)
                        void = input("Press a key to continue")
                        break

                elif int_choice == 58:
                    if mn_lev == 5:
                        print('UMount FreeNas on /media/FreeNas')
                        void = input("Press a key to continue")
                        cmd = "echo \"riky60\" | sudo -S umount /media/FreeNas"
                        os.system(cmd)
                        void = input("Press a key to continue")
                        break

                elif int_choice == 59 :
                    if mn_lev == 5 :
                        print('Mount nfs-low /media/nfs-low')
                        void = input("Press a key to continue")
                        cmd = "echo \"riky60\" | sudo -S mount 192.168.1.144:/media/700Gb /media/nfs-low"
                        os.system(cmd)
                        void = input("Press a key to continue")
                        break

                elif int_choice == 60:
                    if mn_lev == 5:
                        print('UMount nfs-low on /media/nfs-low')
                        void = input("Press a key to continue")
                        cmd = "echo \"riky60\" | sudo -S umount /media/nfs-low"
                        os.system(cmd)
                        void = input("Press a key to continue")
                        break

                elif int_choice == 61:
                    if mn_lev == 5:
                        print('Mount Phenom /media on /media/Phenom')
                        void = input("Press a key to continue")
                        cmd = "echo \"riky60\" | sudo -S mount 192.168.1.183:/media /media/Phenom"
                        os.system(cmd)
                        void = input("Press a key to continue")
                        break

                elif int_choice == 62:
                    if mn_lev == 5:
                        print('UMount Phenom /media on /media/Phenom')
                        void = input("Press a key to continue")
                        cmd = "echo \"riky60\" | sudo -S umount /media/Phenom"
                        os.system(cmd)
                        void = input("Press a key to continue")
                        break

                elif int_choice == 63:
                    if mn_lev == 5:
                        break
                        print('Mount Phenom 2TbF on /media/2TbFb')
                        void = input("Press a key to continue")
                        cmd = "echo \"riky60\" | sudo -S mount 192.168.1.183:/media/2TbFb /media/2TbFb"
                        os.system(cmd)
                        void = input("Press a key to continue")
                        break

                elif int_choice == 64:
                    if mn_lev == 5:
                        break
                        print('UMount Phenom 2TbF on /media/2TbFb')
                        void = input("Press a key to continue")
                        cmd = "echo \"riky60\" | sudo -S umount /media/2TbFb"
                        os.system(cmd)
                        void = input("Press a key to continue")
                        break

                elif int_choice == 65:
                    if mn_lev == 5:
                        break
                        print('Mount Phenom 8TbF on /media/8TbF')
                        void = input("Press a key to continue")
                        cmd = "echo \"riky60\" | sudo -S mount 192.168.1.183:/media/8TbF /media/8TbF"
                        os.system(cmd)
                        void = input("Press a key to continue")
                        break

                elif int_choice == 66:
                    if mn_lev == 5:
                        break
                        print('UMount Phenom 8TbF on /media/8TbF')
                        void = input("Press a key to continue")
                        cmd = "echo \"riky60\" | sudo -S umount /media/8TbF"
                        os.system(cmd)
                        void = input("Press a key to continue")
                        break

                elif int_choice == 67 :
                    if mn_lev == 5 :
                        print('Create a ram disk')
                        size = input("type the size of disk you wish to create (1024m = 1Gb default is 45000m) ")
                        if size == "" :
                            size = "45000m"
                        # void = input("Press a key to continue")
                        cmd = "echo \"riky60\" | sudo -S mount -t tmpfs -o size="+ size +" new_ram_disk /media/ramdsk 1>/dev/null 2>/dev/null"
                        # print(cmd)
                        rslt = os.system(cmd)
                        void = input("Press a key to continue")
                        break

                elif int_choice == 68:
                    if mn_lev == 5:
                        print('UMount /media/ramdsk')
                        void = input("Press a key to continue")
                        cmd = "echo \"riky60\" | sudo -S umount /media/ramdsk 1>/dev/null 2>/dev/null"
                        os.system(cmd)
                        void = input("Press a key to continue")
                        break

                elif int_choice == 69 :
                    if mn_lev == 5 :
                        get_mount_list ()
                        void = input("Press a key to continue")
                        break
                # ====================================================================
                elif int_choice == 71 :
                    if mn_lev == 7 :
                        print('Check the last reboot time')
                        print('last reboot|head -2')
                        void = input("Press a key to continue")
                        cmd = "last reboot|head -2"
                        os.system(cmd)
                        void = input("Press a key to continue")
                        break
                # ====================================================================
                elif int_choice == 72 :
                    if mn_lev == 7 :
                        print('Example of DD copy')
                        print("sudo dd bs=4M if=input of=output status=progress")
                        print("sudo dd bs=4M if=/dev/sdd of=/path/file.img status=progress")
                        void = input("Press a key to continue")
                        # cmd = "last reboot|head -2"
                        # os.system(cmd)
                        # void = input("Press a key to continue")
                        break


                else :
                    mn_lev = mn_lev
                    #mn_lev = 1
                    #continue
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
    title3 =   str_scrname + " " * (num) + "Menu for shell launch" +  archit

    title4 = title1
    print(title1)
    print(title2)
    print(title3)
    print(title4)
# =======================================================================================

set_windows_size ()
get_system_info ()

mn_lev = 1
while True :
    print_menu(mn_lev)
    get_user_input()





