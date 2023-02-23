import pyautogui

while True:
    if pyautogui.hotkey('ctrl', 'alt', '/') or pyautogui.hotkey('/', 'ctrl', 'alt'):
        print('Hello, World')
