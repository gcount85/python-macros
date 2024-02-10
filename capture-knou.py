import pyautogui
import time


pyautogui.FAILSAFE = True


def press_printscreen():
    pyautogui.press('f12')
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


def close_window():
    pyautogui.click(x=-260, y=694, interval=1) 
    pyautogui.press(['command, w'])
    time.sleep(0.5)
    pyautogui.press(['tab, return'])


def open_viewer():
    pyautogui.click(x=-1167, y=603, interval=1) 
    pyautogui.click(x=-873, y=696, interval=1) 
    time.sleep(0.5)
    pyautogui.press(['command, w'])
    time.sleep(0.5)
    pyautogui.click(x=-872, y=153, interval=1) 


def set_viewer():
    pyautogui.click(x=-260, y=694, interval=1) 
    pyautogui.click(x=-503, y=72, interval=1)

# def tgle_open_and_check_end():
#     for _ in range(5):
#         pgdn_and_toggle()
#     if (pyautogui.locateOnScreen('end.png', confidence=0.90)):
#         return
#     else:
#         tgle_open_and_check_end()


# def copy_to_notion():
#     time.sleep(3)

#     pyautogui.tripleClick(x=244, y=322)  # 코딩애플 동영상 제목
#     pyautogui.hotkey('ctrl', 'c', interval=1)

#     # pyautogui.click(x=1192, y=468, interval=1)  # 노션 창으로 이동 및 클릭
#     pyautogui.click(x=1281, y=555, interval=1)  # 노션 창으로 이동 및 클릭
#     pyautogui.press(['enter'])
#     pyautogui.press(['enter'])
#     time.sleep(1)
#     pyautogui.write('/')  # 괄호 안의 문자를 타이핑 합니다.
#     time.sleep(1)
#     pyautogui.press(['down'])
#     pyautogui.press(['enter'])
#     time.sleep(1)
#     pyautogui.hotkey('ctrl', 'v', interval=1)
#     pyautogui.press(['enter'])

#     pyautogui.doubleClick(x=244, y=322)  # 크롬으로 이동 및 클릭

#     tgle_open_and_check_end()
#     pyautogui.hotkey('ctrl', 'a', interval=1)
#     pyautogui.hotkey('ctrl', 'c', interval=1)

#     pyautogui.click(x=1345, y=18, interval=1)  # 노션 내용 칸으로 이동
#     time.sleep(1)
#     pyautogui.hotkey('ctrl', 'v', interval=1)
#     pyautogui.hotkey('ctrl', '[', interval=1)

#     pyautogui.click("next.png", interval=1)  # 다음 강의 가기


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
# Point(x=882, y=917) 옵션 버튼


# pause 문구
# pyautogui.alert('매크로 종료')
