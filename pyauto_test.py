import pyautogui
import pyperclip
import time

print("You have 5 seconds to select the details...")
time.sleep(5)

pyautogui.hotkey("ctrl", "c")
time.sleep(0.5)

details = pyperclip.paste()

with open("details.txt", "w", encoding="utf-8") as f:
    f.write(details)

print("details saved successfully!")
