import tkinter as tk
import os
from dotenv import load_dotenv

load_dotenv()
PIC_PATH = os.getenv("PIC_PATH")

def main():
    window = tk.Tk()
    greeting = tk.Label(text="Hello World!")
    greeting.pack()
    window.mainloop()

if __name__ == '__main__':
    main()