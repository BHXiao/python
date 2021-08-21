import time  # 时间库
from pynput.mouse import Button, Controller as mouse_cl # 鼠标控制器（赋值）
from pynput.keyboard import Key, Controller as key_cl # 键盘控制器


#定义一个函数

def send_message():
    Num = int(input('您要发送多少次：'))
    try_shuru = input('您要发送的内容：')
    time.sleep(3)

    #  1.选定位输入框的位置（鼠标左键点击来实现）
    mouse = mouse_cl()           #获取鼠标的控制权限
    mouse.press(Button.left)     #模拟鼠标左键的按下，鼠标点击事件
    mouse.release(Button.left)   #模拟鼠标左键的弹起

    # 用赤控制发送的次数 rang(5) 重复5次
    # Num = int(input('您要发送多少次：'))
    # try_shuru = input('您要发送的内容：')
    # time.sleep(3)
    for i in range(Num):
        #在输入框中输入文字
        #time.sleep(3)
        Keyboard = key_cl()    #获取键盘的控制权限
        Keyboard.type(try_shuru)  #发送的内容
    # 发送方式  按下回车键发送消息
        Keyboard.press(Key.enter)  #模拟按下回车键
        Keyboard.release(Key.enter) #模拟弹起回车键


time.sleep(3)     # 暂停程序三秒钟
# 调用函数(输入法不同会影响发送的成功与失败)
send_message()
