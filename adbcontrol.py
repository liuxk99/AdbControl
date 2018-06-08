#! /usr/bin/python3

"""
Author: liulei

Version: 1.0

Main Function:
  PC control Android
    The script intercepts the pc's keyboard input and sends the corresponding 
  key value  to the android device using ADB.

Extra Support: Python、ADB
"""

import os
import sys
import tty
import termios
import time


def connect_device(device):
    if device is None:
        device = input('please input android device ip: ')
        if device == '':
            print('emppty ip')
            exit()

    os.system('adb disconnect')

    os.system('sleep 1')
    os.system('adb connect ' + device)

    os.system('sleep 1')
    os.system('adb root')

    os.system('sleep 1')
    os.system('adb connect ' + device)

    os.system('sleep 1')
    os.system('adb remount')

    pass


def process_input():
    print('--------------------------------------------------------')
    print('8(Up),2(Down),4(Left),6(Right),5(Center),1(Back),3(Home)')
    print("'ctrl+d' or 'q' to exist")
    print('--------------------------------------------------------')

    while True:
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        if ord(ch) == 0x3 or ch == 'q':
            print('\n---> stop send key <---')
            break
        else:
            move(ch)


def move(ch):
    asc = ord(ch)
    # print('input key=' + str(ch) + ' ascii=' + str(asc))
    if ch == '8' or asc == 0x41:
        input_event(19)
    elif ch == '2' or asc == 0x42:
        input_event(20)
    elif ch == '4' or asc == 0x44:
        input_event(21)
    elif ch == '6' or asc == 0x43:
        input_event(22)
    elif ch == '5':
        input_event(23)
    elif ch == '1':
        input_event(4)
    elif ch == '3':
        input_event(3)
    pass


key_dict = {19: 'KEY_UP',
            20: 'KEY_DOWN',
            21: 'KEY_LEFT',
            22: 'KEY_RIGHT',
            23: 'KEY_DPAD_CENTER',
            4: 'KEY_BACK',
            3: 'KEY_HOME'}


def input_event(code):
    print("adb shell input keyevent " + key_dict[code])
    os.system('adb shell input keyevent ' + str(code))


def main(argv):
    # host or ip address
    device = None
    if len(argv) > 0:
        device = argv[0]

    connect_device(device)
    process_input()
    pass


if __name__ == '__main__':
    main(sys.argv[1:])
