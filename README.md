# AdbControl
这个工具的设计思想是利用小键盘的布局，通过单手盲操，从而来高效率的控制Adb设备。
+ 方向键（2、4、6、8）
+ 确定键（5）
+ 返回键（1）
+ HOME键（3）

![数字键盘](https://github.com/liuxk99/AdbControl/blob/master/res/dpad.jpg)

# 最佳实践
+ 设备（电视）在视线之内，但是离开发者有一定的距离；
+ 使用遥控器输入对临近的设备有干扰。

# Usage
```
thomas@XancL03:~/bin/adb_control$ ./adbcontrol.py x1
-------- AdbControl: adb tools wrapped by Python  -------
----------- For UserDebug Build with su ----------------
disconnected everything
connected to x1:5555
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
