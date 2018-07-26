#! /usr/bin/python3
# coding=utf-8

# ADB = 'adb'
import os

# ADB = "/home/thomas/Programmer/ADE/Android/SDK/platform-tools/adb"
ADB = 'adb'

def parse_device_name(name):
    device = None
    items = name.split(':')
    if len(items) > 1:
        device = Device(items[0], items[1])
    return device


class Device:
    host = None
    port = None

    def __init__(self, host, port):
        self.host = host
        self.port = port

    def __str__(self):
        if self.host and self.port:
            return self.host + ':' + self.port
        return None

    pass

    def hasHost(self, host):
        return self.host == host


class Serial:
    name = None
    status = None

    device = None

    def __init__(self, name, status):
        self.name = name
        self.status = status
        pass

    def __str__(self):
        name = self.name
        if self.device:
            name = str(self.device)
        return name + '\t' + self.status

    def parse(self, name):
        self.device = parse_device_name(name)

    def find_host(self, host):
        if self.device:
            return self.device.hasHost(host)
        return False

    pass


def get_devices():
    devList = []

    lines = os.popen(ADB + ' devices').readlines()
    count = len(lines)
    if count > 1:
        for i in range(1, count - 1):
            # print("ln: " + lines[i])

            cols = lines[i].split('\t')
            col_len = len(cols)
            if col_len > 1:
                for col in cols:
                    # print("col: " + col)
                    pass

                name = cols[0]
                status = cols[1]
                x1 = Serial(name, status)
                x1.parse(name)
                devList.append(x1)
                # print("serial: " + str(x1))
    return devList
