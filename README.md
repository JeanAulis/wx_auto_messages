# 微信批量自动发送消息

> [!NOTE]
>
> 微信版本：4.0.3.43（其他版本未知，3.x版本可使用wxauto项目，这个项目更好）

> [!IMPORTANT]
>
> 运行中建议不要移动鼠标，运行后需要手动打开微信页面，或者调整合适的位置，一开始建议把搜索框漏出来
>
> 即![search_box.png](https://github.com/JeanAulis/wx_auto_messages/blob/main/search_box.png)
>
> 运行之后有2s来把微信页面置于前台（手慢的话也可以延迟）↓
>
> ```python
> def send_multiple_messages(friend_name, messages):
>     print("准备发送消息...")
>     time.sleep(2)  # 确保微信已经启动并处于前台，你有2秒准备时间
> ```
>
> 使用前请选择合适的窗口大小，并截图替换掉**input_box.png**和**search_box.png**
>
> **（替换后请勿更改窗口大小，页面大小，微信内布局！）**

> [!TIP]
>
> 建议用snipaste截图，或者其他带自动检测窗口元素的截图工具

## 有什么卵用？

该程序基于 ocr 和 键盘鼠标自动化控制 来实现微信自动发送消息的功能。它使用 pyautogui 库进行图像识别，通过比对屏幕截图定位微信界面中的控件（如搜索框和输入框），并模拟鼠标点击与键盘输入操作。同时，利用 pyperclip 库实现剪贴板操作，将消息内容复制到剪贴板并粘贴到微信的输入框中，最后模拟回车键发送消息。通过循环结构，程序能够自动化地向指定好友发送多条消息，并支持指定消息重复发送的次数。



克隆本项目：

```bash
git clone https://github.com/JeanAulis/wx_auto_messages.git
```

或者下载`ocrauto.py`和`search_box.png`以及`input_box.png`这三个即可



需安装以下库：

```bash
pip install pyautogui
```

```bash
pip install pyperclip
```

根据需要修改`all_repetition`、`repetiton`、`friend_name`、`messages`

```python
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
```

```python
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
```

> [!WARNING]
>
> 请勿进行消息轰炸，本程序仅供娱乐，请勿用于其他用途



## 可能出现的问题

- 一开始运行时没反应/报错
- 可能搜出来不对的联系人
- 发送过快导致卡顿，发送失败（请自行添加`time.sleep()`）
- 其他没发现的

能力有限，有啥问题放AI解决吧



## 最后

咳咳，懒得改了，自己在源代码上面修改吧，不会QT，这只是一种解决方法，大佬们有更好的解决方法更好



## 免责声明
代码仅供交流学习使用，请勿用于非法用途和商业用途！如因此产生任何法律纠纷，均与作者无关！
