# AdbControl
computer control android device

# Usage
```
thomas@XancL03:~/bin/adb_control$ ./adbcontrol.py x1
-------- AdbControl: adb tools wrapped by Python  -------
----------- For UserDebug Build with su ----------------
disconnected everything
connected to x1:5555
adbd is already running as root
already connected to x1:5555
remount succeeded
--------------------------------------------------------
8(Up),2(Down),4(Left),6(Right),5(Center),1(Back),3(Home)
'ctrl+d' or 'q' to exist
--------------------------------------------------------
adb shell input keyevent KEY_RIGHT
adb shell input keyevent KEY_RIGHT
adb shell input keyevent KEY_UP
adb shell input keyevent KEY_DOWN
adb shell input keyevent KEY_LEFT
adb shell input keyevent KEY_DPAD_CENTER
adb shell input keyevent KEY_HOME

---> stop send key <---

```
