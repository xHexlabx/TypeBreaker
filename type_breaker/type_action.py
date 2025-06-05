from pyautogui import typewrite

def type_text(text: str):  # <--- เปลี่ยนชื่อฟังก์ชันเป็น type_text
    typewrite(text, interval=0.05)