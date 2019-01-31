#! /usr/bin/python3

"""
Author: liulei

Version: 1.0

Author: Thomas Liu(liuxk99@gmail.com)
Version: 1.1

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
from time import sleep

def connect_device(device):
    if device is None:
        device = input('please input android device ip or host name: ')
        if device == '':
            print('ERROR: empty ip or host name!')
            exit()

    os.system('adb disconnect')

    os.system('sleep 1')
    os.system('adb connect ' + device)

    # os.system('sleep 1')
    # os.system('adb root')
    #
    # os.system('sleep 1')
    # os.system('adb connect ' + device)
    #
    # os.system('sleep 1')
    # os.system('adb remount')

    pass


def process_input():
    i = 0
    cmd_line = 'adb shell am start -S -W -n com.stv.signalsourcemanager/.MainActivity'
    cmd_line1 = 'adb shell am start -n com.stv.signalsourcemanager/.MainActivity'
    print(cmd_line)
    os.system(cmd_line)
    sleep(15)

    while True:
        i = i + 1
        print('==>round: %03d' % i)

        os.system(cmd_line1)
        sleep(5)
        
        input_event(22)
        sleep(3)
        
        if i > 20:
            break
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
    print('-------- SignalSource Benchmarks: wrapped by Python  -------')

    # host or ip address
    device = None
    if len(argv) > 0:
        device = argv[0]

    connect_device(device)
    process_input()
    pass


if __name__ == '__main__':
    main(sys.argv[1:])
