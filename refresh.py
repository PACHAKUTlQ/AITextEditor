import pyautogui
import time
import os

# Set the coordinates of the address bar where you type the URL
# address_bar_x = 100
# address_bar_y = 100

# Set the URL of the extension popup page
popup_url = "extension://ddlbpiadoechcolndfeaonajmngmhblj/popup.html"

os.startfile("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")

# Move the mouse to the address bar and click
# pyautogui.moveTo(address_bar_x, address_bar_y)
# pyautogui.click()
time.sleep(1)

# Type the URL of the extension popup page
pyautogui.typewrite(popup_url)
time.sleep(1.5)
pyautogui.press('enter')

# Open dev-tools console
pyautogui.hotkey('ctrl', 'shift', 'j')
# Move to the dev-tools console and click
console_x = 2000
console_y = 1000
pyautogui.moveTo(console_x, console_y)
time.sleep(2)
pyautogui.click()
time.sleep(0.5)
pyautogui.typewrite('localStorage.clear()')
pyautogui.press('enter')
time.sleep(1)
# Close the browser window
pyautogui.hotkey('ctrl', 'w')