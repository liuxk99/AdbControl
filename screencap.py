#! /usr/bin/python3

"""
Author: Thomas Liu(liuxk99@gmail.com)
Version: 1.0

Main Function:
  wrap for screencap -p /sdcard/xxx.png

Extra Support: Python、ADB
"""

import os
import sys
import tty
import termios
import time


def capture_png(device, png_file):
    if device is None:
        device = input('please input android device ip or host name: ')
        if device == '':
            print('ERROR: empty ip or host name!')
            exit()
    if png_file is None:
        print('ERROR: empty png file name!')
        exit(-1)

    os.system('adb disconnect')

    os.system('sleep 1')
    os.system('adb connect ' + device)

    os.system('sleep 1')
    os.system('adb shell screencap -p /sdcard/' + png_file);
    os.system('adb pull /sdcard/' + png_file)
    pass

def main(argv):
    print('-------- screencap: screen capture tools wrapped by Python  -------')

    # host or ip address
    device = None
    png_file = None
    if len(argv) > 0:
        device = argv[0]
        png_file = argv[1]

    capture_png(device, png_file)
    pass


if __name__ == '__main__':
    main(sys.argv[1:])
