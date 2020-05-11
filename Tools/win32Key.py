import win32api
import win32con


class KeyboardKeys(object):
    """
A 65    0 48    F1 112    Backspace 8
B 66    1 49.   F2 113    Tab 9
C 67    2 50.   F3 114.   Clear 12
D 68    3 51.   F4 115.   Enter 13
E 69    4 52.   F5 116.   Shift 16
F 70    5 53.   F6 117.   Control 17
G 71    6 54    F7 118.   Alt 18
H 72    7 55.   F8 119.   Caps Lock 20
I 73    8 56.   F9 120.   Esc 27
J 74    9 57.   F10 121.  Spacebar 320
K 75    * 106   F11 122.  Page Up 33
L 76    + 107.  F12 123.  Page Down 34
M 77    ENTER 108.        End 35
N 78     - 109            Home 36
O 79     . 110            Left Arrow 37
P 80     / 111.           Up Arrow 38
Q 81     0 96.            Right Arrow 39
R 82.    1 97             Down Arrow 40
S 83.    2 98             Insert 45
T 84.    3 99.            Delete 46
U 85.    4 100            Help 47
V 86.    5 101            Num Lock 144
W 87.    6 102
X 88.    7 103
Y 89.    8 104
Z 90.    9 105
    """
    # 模拟键盘按键类
    VK_CODE = {
        'enter': 0x0D,
        'ctrl': 0x11,
        'v': 0x56,
        'up': 0x26,
        'down': 0x28
    }

    @staticmethod
    def keyDown(keyName):
        # 按下按键
        win32api.keybd_event(KeyboardKeys.VK_CODE[keyName], 0, 0, 0)

    @staticmethod
    def keyUp(keyName):
        # 释放按键
        win32api.keybd_event(KeyboardKeys.VK_CODE[keyName], 0, win32con.KEYEVENTF_KEYUP, 0)

    @staticmethod
    def oneKey(key):
        # 模拟单个按键
        KeyboardKeys.keyDown(key)
        KeyboardKeys.keyUp(key)

    @staticmethod
    def twoKeys(key1, key2):
        # 模拟两个组合键
        KeyboardKeys.keyDown(key1)
        KeyboardKeys.keyDown(key2)
        KeyboardKeys.keyUp(key2)
        KeyboardKeys.keyUp(key1)
