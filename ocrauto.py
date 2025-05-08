# -*- coding: utf-8 -*-
"""
    默认此程序仅能在全屏下使用
    如需修改，请自行替换掉
        search_box.png
        input_box.png
    自行调整分辨率
"""

import pyautogui
import pyperclip
import time


all_repetition = 2 #整个messages发送的次数
repetiton = 1 #一条消息重复次数
friend_name = '文件传输助手' #自行填写
messages = [
    "你就是个不值一提的渣渣，别再让我看到你！",
    "看看你那副样子，真是我见过最丑的东西了。",
    "别再装了，真想把你从这个世界抹去。",
    "你这么低能，居然敢站在我面前？",
    "闭嘴，你的存在已经让我觉得恶心！"
]

# 发送消息的主函数
def send_multiple_messages(friend_name, messages):
    print("准备发送消息...")
    time.sleep(2)  # 确保微信已经启动并处于前台，你有2秒准备时间

    # 找到搜索框并点击
    print("查找搜索框...")
    search_box_location = pyautogui.locateOnScreen("search_box.png", confidence=0.8)
    if search_box_location:
        pyautogui.click(pyautogui.center(search_box_location))  # 点击搜索框
        print("搜索框已点击")
    else:
        print("未找到搜索框图像，请检查截图或微信界面")
        return

    # 使用 pyperclip 输入中文
    pyperclip.copy(friend_name)  # 将联系人名称复制到剪贴板
    pyautogui.hotkey('ctrl', 'v')  # 粘贴到输入框
    time.sleep(1)
    pyautogui.press("enter")  # 按回车键进入聊天

    # 等待微信加载联系人聊天页面
    time.sleep(1)

    # 找到聊天输入框并点击
    print("查找输入框...")
    input_box_location = pyautogui.locateOnScreen("input_box.png", confidence=0.8)
    if input_box_location:
        pyautogui.click(pyautogui.center(input_box_location))  # 点击输入框
        print("输入框已点击")
    else:
        print("未找到输入框图像，请检查截图或微信界面")
        return

    #整个messages发送的次数
    for _ in range(all_repetition):
        # 循环发送多条消息
        for message in messages:
            print(f"发送消息：{message}")

            #此for循环实现一条语句发多次
            for _ in range(repetiton):
                # 使用 pyperclip 输入消息内容
                pyperclip.copy(message)  # 将消息内容复制到剪贴板
                pyautogui.hotkey('ctrl', 'v')
                pyautogui.press("enter")
                # time.sleep(1)


    print(f"多条消息已发送给「{friend_name}」")

if __name__ == '__main__':
    send_multiple_messages(friend_name, messages)