import pyautogui
import time

# 영상 다운로드 버튼 클릭


def download_video():
    time.sleep(4)
    # pyautogui.click('다운로드화살표.png', interval=1)
    pyautogui.moveTo(x=1767, y=278)  # 다운로드 화살표
    pyautogui.click(interval=1)
    pyautogui.moveTo(x=1667, y=259)
    time.sleep(1)
    pyautogui.click(interval=1)  # mp4 hd 클릭
    time.sleep(2)
    # pyautogui.click('mp41080hd.png', interval=1)
    # pyautogui.moveTo(x=1200, y=916)  # 완료 버튼
    # pyautogui.click(interval=1)
    # time.sleep(1.5)
    pyautogui.moveTo(x=1815, y=915)  # 다음 강의 포지션
    pyautogui.click(interval=1)
    # pyautogui.click('다음강의.png', interval=1)


num = 200     # 몇 회 반복할 건지 설정
for f in range(num):
    download_video()


# 현재 마우스 위치 출력
# print(pyautogui.position())


# pause 문구
pyautogui.alert('매크로 종료')
