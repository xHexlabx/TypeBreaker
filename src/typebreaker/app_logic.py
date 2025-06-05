from .ocr import ocr  # <--- ปรับ import
from .type_action import type_text  # <--- ปรับ import
from .screen_capture import screen_capture  # <--- ปรับ import

import time
import keyboard

SCREEN_POSITION = {
    "x1": 432,
    "y1": 800,
    "x2": 2600,
    "y2": 900,
}

def start_app():
    print("TypeBreaker is ready. Press Enter to start, and press Enter again to stop. 🎯")
    keyboard.wait("enter")
    print("TypeBreaker is running 🤖")

    time.sleep(2)

    while True:
        if keyboard.is_pressed("enter"):
            print("TypeBreaker is stopping...")
            break

        screenshot = screen_capture(**SCREEN_POSITION)
        text_content = ocr(screenshot) # เปลี่ยนชื่อตัวแปรเพื่อความชัดเจน
        type_text(text_content) # เรียกใช้ฟังก์ชันที่เปลี่ยนชื่อแล้ว

        time.sleep(1)
        keyboard.press_and_release('tab+enter')
        time.sleep(1)
