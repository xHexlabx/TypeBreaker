# TypeBreaker 🐵

## Monkey Type Typing Bot (OCR-Powered) 🤖

TypeBreaker is a Python project designed to enhance WPM (Words Per Minute) scores specifically on the **Monkey Type** platform. By integrating **OCR (Optical Character Recognition)** technology with **`pytesseract`**, this project can "read" the words displayed on the Monkey Type webpage and automatically perform the typing actions.

### Key Features:

  * **OCR-Powered Typing:** Utilizes `pytesseract` to detect and convert text from images on Monkey Type into machine-readable data.
  * **Automated WPM Scoring:** Helps users achieve faster and more accurate WPM scores on Monkey Type.
  * **Python-based:** Developed using Python, making it easy to understand, customize, and extend.

### Technologies Used:

  * **Python:** The primary programming language used for development.
  * **Pytesseract:** A Python library for interacting with the Tesseract OCR Engine.

### Project Objective:

This project was created for the purpose of studying and exploring the feasibility of using OCR to interact with websites, particularly in the context of typing games or tests.

-----

## How to Use TypeBreaker

Follow these steps to get TypeBreaker up and running on your machine.

### Prerequisites

Before you begin, make sure you have the following installed:

  * **Python 3.x:** TypeBreaker is built with Python.
  * **Tesseract OCR Engine:** `pytesseract` is a Python wrapper for Tesseract. You'll need to install the Tesseract OCR engine itself on your system.
      * For **Windows**: Download the installer from [Tesseract-OCR GitHub](https://www.google.com/search?q=https://github.com/UB-Mannheim/tesseract/wiki).
      * For **macOS**: `brew install tesseract`
      * For **Linux (Debian/Ubuntu)**: `sudo apt-get install tesseract-ocr`

### Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/YOUR_USERNAME/TypeBreaker.git
    cd TypeBreaker
    ```

    (Replace `YOUR_USERNAME` with your actual GitHub username or the repository's path.)

2.  **Create and activate a virtual environment:**
    It's recommended to use a virtual environment to manage project dependencies.

    ```bash
    python -m venv venv
    # On Windows:
    .\venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

### Running TypeBreaker

After installation, you can run the bot using the provided script.

1.  **Navigate to the project root:**
    If you're not already there, change your directory to the `TypeBreaker` root folder (where `README.md` is located).

2.  **Execute the `run_typebreaker.py` script:**

    ```bash
    python scripts/run_typebreaker.py
    ```

    Upon running, the script will guide you through the process, which typically involves:

      * Opening your web browser to Monkey Type.
      * (Potentially) requiring you to adjust the Monkey Type settings for optimal OCR.
      * Automatically recognizing and typing the words.

### Tips for Optimal Performance

  * **Screen Resolution:** Ensure your screen resolution is consistent, as OCR can sometimes be sensitive to changes in element sizing.
  * **Browser Zoom:** Keep your browser zoom level at 100% on Monkey Type for the best OCR accuracy.
  * **Monkey Type Theme/Settings:** Simple and high-contrast themes on Monkey Type tend to yield better OCR results. Avoid themes with complex backgrounds or highly stylized fonts.
  * **Test Environment:** It's best to run TypeBreaker on a dedicated screen or window where no other applications overlap the Monkey Type interface.

-----
