import tkinter as tk
import os
from dotenv import load_dotenv

load_dotenv()
PIC_PATH = os.getenv("PIC_PATH")

def main():
    print(PIC_PATH)

if __name__ == '__main__':
    main()