# screencap
对于某些设备来说，DDMS(Android Studio)的capture screen功能截取的图片是空的，而使用screencap却可以截取到内容。
因为screencap与DDMS使用了不同的方式来实现截屏，我们可以对该命令进行封装。
For some device, DDMS(Android Studio) captrue screen can't get valid screen content, but screencap command will get screen context.
That because the implementation of capturing is different, so we can wrap this command.

+ 在设备上将截图保存为文件； Save the captured content as PNG file on the device.
+ 把然后pull出来。Pull the PNG file from device to local file.

即：
```
adb shell screencap -p /sdcard/xxx.png
adb pull /sdcard/xxx.png ./xxx.png
```

# Usage
+ first parameter：host or ip
+ second parameter: file name

```
thomas@XancL03:~/bin/adb_control$ screencap.py x1 xxx.png
-------- screencap: screen capture tools wrapped by Python  -------
* daemon not running; starting now at tcp:5037
* daemon started successfully
disconnected everything
connected to x1:5555
/sdcard/xxx.png: 1 file pulled. 2.7 MB/s (1107858 bytes in 0.388s)

```

