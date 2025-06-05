import sys
import os

# เพิ่ม src directory เข้าไปยัง Python path เพื่อให้ import package typebreaker ได้
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from typebreaker.app_logic import start_app

if __name__ == "__main__":
    start_app()