import colorama
from colorama import Fore, Back, Style
import os
import socket
import phonenumbers
import requests
from phonenumbers import geocoder
import os

print("""\033[40m\33[35m

.##..##...####...#####...........######...####....####...##......##..##.
.##..##..##..##..##..##............##....##..##..##..##..##.......####..
.##..##..######..##..##............##....##..##..##..##..##........##...
..####...##..##..##..##............##....##..##..##..##..##.......####..
...##.....####...#####...######....##.....####....####...######..##..##.
........................................................................""")



def main():

    print("")
    n = input("1-Ip-Web-Track\n\n\n2-Tracker ip \n\n\n3-Num-Tracker(isp)\n\n\n\n\n\nChoise a Number : ")
    if n == '1' :
          trackweb()

    if n =='2' :
          tracker()
    if n=='3' :
          numtrack ()


def tracker():
    os.system("clear")
    os.system("python2 dont_open.py")
    os.system("python2 v0d_ip_tracker.py")

def trackweb():
    os.system("clear")

    print("""\033[40m\33[32m

        #####                     #     #           #
          #                       #     #           #
          #     ######            #     #   #####   ######
          #     #     #           #  #  #  #     #  #     #
          #     #     #\33[33m]   # # # #  #######  #     #
          #     #     #           ##   ##  #        #     #
        #####   ######            #     #   #####   ######
                #        #######
                # """)





    print("")
    print(socket.gethostbyname(input('        hostweb name:      ')))


def numtrack():
    os.system("clear")
    print("""_________        .------______-------.
:______.-':      :  .--------------.  :
| ______  |      | :                : |
|:______B:|      | |  Num-Tracker   | |
|:______B:|      | |  by caableyz   | |
|:______B:|      | |                | |
|         |      | |                | |
|:_____:  |      | |                | |
|    ==   |      | :                : |
|       O |      :  '--------------'  :
|       o |      :'---...______...---'
|       o |-._.-i___/'             \._
|'-.____o_|   '-.   '-...______...-'  `-._
:_________:      `.____________________   `-.___.-.
                 .'.eeeeeeeeeeeeeeeeee.'.      :___:
               .'.eeeeeeeeeeeeeeeeeeeeee.'.
              :____________________________:""")

    print("")
    print("ex to track : +33656456756")
    print("")
    your_ph_num = input('Enter Number To track ! : ')
    phone_number = phonenumbers.parse(your_ph_num)
    print(geocoder.description_for_number(phone_number,
                                          'en'))
    from phonenumbers import carrier
    service_provider = phonenumbers.parse(your_ph_num)
    print(carrier.name_for_number(service_provider,
                                  'en'))




if __name__=='__main__':
              main()
