import pyautogui
import time


pyautogui.FAILSAFE = True
screen_shot_key = 'f12'


def press_printscreen():
    pyautogui.press(screen_shot_key)
    # with pyautogui.hold(['shiftleft, command']):
    #     pyautogui.press(['5'])


def save_document():
    pyautogui.click(x=882, y=917, interval=1) 
    pyautogui.press(['down, down'])
    time.sleep(0.5)
    pyautogui.press(['return'])
    time.sleep(0.5)
    pyautogui.press(['return'])


def go_next_page():
    pyautogui.click(x=-260, y=694, interval=1) 
    pyautogui.press('right')


# def close_window():
#     pyautogui.click(x=-260, y=694, interval=1) 
#     pyautogui.press(['command, w'])
#     time.sleep(0.5)
#     pyautogui.press(['tab, return'])


# def open_viewer():
#     pyautogui.click(x=-1167, y=603, interval=1) 
#     pyautogui.click(x=-873, y=696, interval=1) 
#     time.sleep(0.5)
#     pyautogui.press(['command, w'])
#     time.sleep(0.5)
#     pyautogui.click(x=-872, y=153, interval=1) 


# def set_viewer():
#     pyautogui.click(x=-260, y=694, interval=1) 
#     pyautogui.click(x=-503, y=72, interval=1)


num = 41     # 몇 회 반복할 건지 설정
# num = 1     # 몇 회 반복할 건지 설정
for f in range(num):
    press_printscreen()
    time.sleep(0.5)
    save_document()
    time.sleep(0.5)
    go_next_page()
    time.sleep(0.5)
    # close_window()
    # time.sleep(0.5)
    # open_viewer()
    # time.sleep(0.5)
    # set_viewer()
    # time.sleep(0.5)


# 현재 마우스 위치 출력
# print(pyautogui.position())


# pause 문구
# pyautogui.alert('매크로 종료')
