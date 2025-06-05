from setuptools import setup, find_packages

# อ่านเนื้อหาจาก README.md สำหรับ long_description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# อ่าน dependencies จาก requirements.txt
with open("requirements.txt", "r", encoding="utf-8") as f:
    requirements = f.read().splitlines()

setup(
    name="type_breaker",
    version="0.1.0",  # เวอร์ชั่นของโปรเจกต์
    author="HexTex",  # <--- ใส่ชื่อของคุณ
    author_email="tee.hemjinda.work@gmail.com",  # <--- ใส่อีเมลของคุณ
    description="A Monkey Type typing bot using OCR.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/type_breaker",  # <--- URL ของโปรเจกต์ (ถ้ามี)
    package_dir={'': 'src'},  # บอกว่า package อยู่ใน src/
    packages=find_packages(where='src'),  # ค้นหา packages ทั้งหมดใน src/
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # <--- เลือก License ที่เหมาะสม
        "Operating System :: OS Independent",
        "Topic :: Utilities",
        "Development Status :: 3 - Alpha", # หรือ 4 - Beta
    ],
    python_requires='>=3.6',  # <--- เวอร์ชั่น Python ที่ต้องการ
    install_requires=requirements,  # Dependencies ที่อ่านมาจาก requirements.txt
    entry_points={
        'console_scripts': [
            'type_breaker=type_breaker.app_logic:start_app', # <--- ทำให้รันจาก command line ได้ด้วยคำสั่ง type_breaker
        ],
    },
    project_urls={  # (Optional)
        'Bug Reports': 'https://github.com/yourusername/TypeBreaker/issues',
        'Source': 'https://github.com/yourusername/TypeBreaker/',
    },
)