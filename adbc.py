#! /usr/bin/python3
# coding=utf-8

"""
Author: Thomas Liu(liuxk99@gmail.com)
Version: 1.0

Main Function:
  wrap for adb connect, root, remount

Extra Support: Python、ADB
"""

import os
import sys
import tty
import termios
import time

import device
from device import ADB


def adbc(host):
    if host is None:
        host = input('please input android device ip or host name: ')
        if host == '':
            print('ERROR: empty ip or host name!')
            exit()

    dev_list = device.get_devices()

    target = ''
    serial = ''
    for dev in dev_list:
        if dev.find_host(host):
            target = str(dev.device)
            # print(target)
            serial = '-s ' + target + ' '
            break

    if target:
        # disconnect
        os.system(ADB + ' disconnect' + ' ' + target)

    # connect
    os.system('sleep 1')
    os.system(ADB + ' connect ' + host)

    # root
    os.system('sleep 1')
    os.system(ADB + ' ' + serial + 'root')

    # reconnect
    os.system('sleep 1')
    os.system(ADB + ' connect ' + host)

    # remount
    os.system('sleep 1')
    os.system(ADB + ' ' + serial + 'remount')

    pass


def main(argv):
    print('-------- adbc: adb connect tools wrapped by Python  -------')

    # host or ip address
    host = None
    if len(argv) > 0:
        host = argv[0]

    adbc(host)
    pass


if __name__ == '__main__':
    main(sys.argv[1:])

    # lines = os.popen("ps -C colord | grep -v CMD | awk '{ print $1 }'").readlines()
    # print (lines[0])
    pass
