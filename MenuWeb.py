"""
implementation of a program to manage user choices

"""
# cp /home/riky60/PycharmProjects/Prj01/Menu01.py  /home/riky60/Shell/Python

import csv
import datetime
import subprocess
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
# item and row to hilight
hitem = 1
rowtem = 1

print(type(RELEASE_DATA))
for key, x in RELEASE_DATA :
    print(key)
    print(x)

print("==========================================================================")
len_delimiter = 100
script_name = os.path.basename(__file__)
user = os.environ.get('USER')
pc_user = "riky60"
# pc_user = "pi"
#logging.basicConfig(filename='Menu01.log', encoding='utf-8', level=logging.INFO)
# logging.debug('This message should go to the log file')
# logging.info('So should this')
# logging.warning('And this, too')
# logging.error('And non-ASCII stuff, too, like Øresund and Malmö')

#
#
#
#
#
#
#sudo mousepad /etc/minidlna.conf
#

#=======================================================================================
menu01 = {
    1: "Mount Rpi3B+Download", 2: "Umount Rpi3B+Download", 3: "Mount /var/www/html/mnt", 4: "Umount /var/www/html/mnt",
    5: "Mount /media/FreeNas", 6: "Umount /media/FreeNas", 7: "minidlna status", 8: "restart minidlna", 9: "hdparm", 10: "",
    11: "", 12: "", 13: "", 14: "", 15: "sudo mousepad /etc/minidlna.conf", 16: "",
    17: "", 18: "", 19: "", 20: "", 21: "", 50: ""
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

#=======================================================================================

def print_menu(mnu):

    sprtr = chr(124)  # separator char
    if user == pc_user :
        hlf_scr = 40   # half screen value
    else :
        hlf_scr = 28  # half screen value
    if mnu == 1 :     # menu level
        menu_options = menu01
    elif mnu == 3 :
        menu_options = menu30
    elif mnu == 5:
        menu_options = menu50
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
                exit(0)
            elif mn_lev == 3 :
                mn_lev = 1
            elif mn_lev == 5 :
                mn_lev = 1
            break
        elif (choice == '' ) :
            break
        else :
            if len(result) > 0 and ((int(choice) > 0) or (int(choice) < 99)):
                int_choice = int(choice)

                if int_choice == 1 :
                    if mn_lev == 1 :
                        cmd = "sudo mount 192.168.1.164:/ /media/Rpi3B+Download"
                        os.system(cmd)
                # ====================================================================
                if int_choice == 2 :
                    if mn_lev == 1 :
                        cmd = "sudo umount /media/Rpi3B+Download"
                        os.system(cmd)

                # ====================================================================
                if int_choice == 3 :
                    if mn_lev == 1:
                        cmd = "sudo mount 192.168.1.164:/ /var/www/html/mnt"
                        os.system(cmd)
                        void = input("Press a key to continue")
                    break
                # ====================================================================
                if int_choice == 4 :
                    if mn_lev == 1:
                        cmd = "sudo umount /var/www/html/mnt"
                        os.system(cmd)
                        void = input("Press a key to continue")

                    break
                # ====================================================================
                if int_choice == 5 :
                    if mn_lev == 1:
                        print('UMount Phenom 2TbF on /media/2TbFb')
                        cmd = "sudo mount 192.168.1.151:/mnt/FreeNas12Tb /media/FreeNas"
                        os.system(cmd)
                        void = input("Press a key to continue")

                    break
                # ====================================================================
                if int_choice == 6 :
                    if mn_lev == 1:
                        print('UMount Phenom 2TbF on /media/2TbFb')
                        cmd = "sudo umount /media/FreeNas"
                        os.system(cmd)
                        void = input("Press a key to continue")

                    break
                # ====================================================================
                if int_choice == 7 :
                    if mn_lev == 1:
                        #print('UMount Phenom 2TbF on /media/2TbFb')
                        cmd = "sudo service minidlna status"
                        os.system(cmd)
                        void = input("Press a key to continue")
                    #
                    break
                # ====================================================================
                if int_choice == 8 :
                    if mn_lev == 1:
                        #print('UMount Phenom 2TbF on /media/2TbFb')
                        cmd = "sudo systemctl restart minidlna"
                        os.system(cmd)
                        void = input("Press a key to continue")
                    break

                # ====================================================================
                if int_choice == 9 :
                    if mn_lev == 1:
                        print('sudo hdparm -S 120 /dev/sda')
                        cmd = "sudo hdparm -S 120 /dev/sda"
                        os.system(cmd)
                        void = input("Pres a key to continue")
                    break

                # ====================================================================
                if int_choice == 10 :
                    if mn_lev == 1:
                        #print('UMount Phenom 2TbF on /media/2TbFb')
                        cmd = "sudo systemctl restart minidlna"
                        os.system(cmd)
                    break

                # ====================================================================
                if int_choice == 15 :
                    if mn_lev == 1:
                        #print('sudo mousepad /etc/minidlna.conf')
                        cmd = "sudo mousepad /etc/minidlna.conf"
                        os.system(cmd)
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
                    #mn_lev = 5
                    break
                # ====================================================================
                elif int_choice == 51 :
                    if mn_lev == 5 :
                        print('Mount Raspberry Pi  on /media/Rpi3B+Download')
                        void = input("Press a key to continue")
                        cmd = "echo \"riky60\" | sudo -S mount -vvvv -o nfsvers=4 192.168.1.164:/ /media/Rpi3B+Download 1>/dev/null 2>/dev/null"
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
                else :
                    mn_lev = mn_lev
                    #mn_lev = 1
                    #continue
                break
            else :
                continue


# =======================================================================================
def display_title_bar() :
    iptime = subprocess.run(["uptime", "-p"], stdout=subprocess.PIPE)
    uptime = iptime.stdout.decode()

    if user == pc_user :
        len_delimiter = 100
    else :
        len_delimiter = 64
    curr_time = datetime.datetime.now()
    screen_clear()
    title1 = Fore.LIGHTYELLOW_EX + "=" * len_delimiter + Style.RESET_ALL
    release = Fore.RED + RELEASE_DATA['NAME'] + ' ' + RELEASE_DATA['VERSION'] + Style.RESET_ALL
    name_len = len(RELEASE_DATA['VERSION_CODENAME'])
    if user == pc_user:
        title2 = str(curr_time)[: 19] + " " * 19 + release + " " * (20 - name_len) \
                 + "Ubuntu code name >" + Fore.LIGHTGREEN_EX + RELEASE_DATA['VERSION_CODENAME'] + \
                 Style.RESET_ALL + "<"
    else :
        title2 = str(curr_time)[: 16] + " " * 2 + release + " " * (8 - name_len) \
                + "code nm " + Fore.LIGHTGREEN_EX + RELEASE_DATA['VERSION_CODENAME'] + \
                 Style.RESET_ALL + ""


    if user == pc_user:
        str_scrname = "script name " + script_name
        num = 40 - len(str_scrname)
        str_scrname = "script name " + Fore.RED + script_name + Fore.RESET
    else :
        str_scrname = "scrp name " + script_name
        num = 30 - len(str_scrname)
        str_scrname =  Fore.RED + script_name + Fore.RESET


    if user == pc_user:
        num1 = 39 - len(" Archit : ") - len(arch[0])
    else :
        num1 = 19 - len(" Archit : ") - len(arch[0])

    archit = " " * (num1) + " Archit : " + Fore.LIGHTGREEN_EX + arch[0] + Fore.RESET
    if user == pc_user:
        title3 =   str_scrname + " " * (num) + "Menu for shell launch" +  archit
    else:
        title3 = str_scrname + " " * (num + 1) + "Shell Menu " + archit
    title4 = "uptime is : " + uptime.strip()

    title5 = title1
    print(title1)
    print(title2)
    print(title3)
    print(title4)
    print(title5)
# =======================================================================================

set_windows_size ()
get_system_info ()

mn_lev = 1
while True :
    print_menu(mn_lev)
    get_user_input()

