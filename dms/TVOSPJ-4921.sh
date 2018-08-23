KEY_UP=19
KEY_DOWN=20
KEY_LEFT=21
KEY_RIGHT=22
KEY_DPAD_CENTER=23

adb shell am force-stop com.letv.tvos.appstore

sleep 3
adb shell am start -W -n com.letv.tvos.appstore/.appmodule.storesearch.StoreSearchActivity
source build/envsetup.sh
pid com.letv.tvos.appstore

sleep 1
# Q
adb shell input keyevent $KEY_DOWN
adb shell input keyevent $KEY_LEFT
adb shell input keyevent $KEY_DPAD_CENTER

sleep 2
# w
adb shell input keyevent $KEY_RIGHT
adb shell input keyevent $KEY_DOWN
adb shell input keyevent $KEY_DPAD_CENTER

sleep 2
adb shell input keyevent $KEY_LEFT
adb shell input keyevent $KEY_LEFT
adb shell input keyevent $KEY_DOWN
adb shell input keyevent $KEY_DPAD_CENTER

sleep 2
adb shell input keyevent $KEY_RIGHT
adb shell input keyevent $KEY_RIGHT
adb shell input keyevent $KEY_RIGHT
adb shell input keyevent $KEY_RIGHT
adb shell input keyevent $KEY_RIGHT
adb shell input keyevent $KEY_RIGHT

sleep 2
adb shell input keyevent $KEY_DPAD_CENTER

adb logcat -c
sleep 4
adb shell input keyevent $KEY_DPAD_CENTER
