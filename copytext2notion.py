import pyautogui
import time


pyautogui.FAILSAFE = True


def pgdn_and_toggle():
    """
    1회 pgdn 누르고, 토글 찾음
    """
    pyautogui.press(['pgdn'])
    time.sleep(0.5)
    try:
        while True:
            time.sleep(1)
            loc_tglex, loc_tgley = pyautogui.locateCenterOnScreen(
                'toggle.png', confidence=0.8)
            time.sleep(1)
            pyautogui.click(x=loc_tglex, y=loc_tgley)
    except TypeError:
        return


def tgle_open_and_check_end():
    for _ in range(5):
        pgdn_and_toggle()
    if (pyautogui.locateOnScreen('end.png', confidence=0.90)):
        return
    else:
        tgle_open_and_check_end()


def copy_to_notion():
    time.sleep(3)

    pyautogui.tripleClick(x=244, y=322)  # 코딩애플 동영상 제목
    pyautogui.hotkey('ctrl', 'c', interval=1)

    # pyautogui.click(x=1192, y=468, interval=1)  # 노션 창으로 이동 및 클릭
    pyautogui.click(x=1281, y=555, interval=1)  # 노션 창으로 이동 및 클릭
    pyautogui.press(['enter'])
    pyautogui.press(['enter'])
    time.sleep(1)
    pyautogui.write('/')  # 괄호 안의 문자를 타이핑 합니다.
    time.sleep(1)
    pyautogui.press(['down'])
    pyautogui.press(['enter'])
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'v', interval=1)
    pyautogui.press(['enter'])

    pyautogui.doubleClick(x=244, y=322)  # 크롬으로 이동 및 클릭

    tgle_open_and_check_end()
    pyautogui.hotkey('ctrl', 'a', interval=1)
    pyautogui.hotkey('ctrl', 'c', interval=1)

    pyautogui.click(x=1345, y=18, interval=1)  # 노션 내용 칸으로 이동
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'v', interval=1)
    pyautogui.hotkey('ctrl', '[', interval=1)

    pyautogui.click("next.png", interval=1)  # 다음 강의 가기


num = 100     # 몇 회 반복할 건지 설정
for f in range(num):
    copy_to_notion()


# 현재 마우스 위치 출력
# print(pyautogui.position())


# pause 문구
pyautogui.alert('매크로 종료')
