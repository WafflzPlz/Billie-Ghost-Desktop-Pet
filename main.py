import tkinter as tk
import os
from dotenv import load_dotenv

load_dotenv()
PIC_PATH = os.getenv("PIC_PATH")

def main():
    master = tk.Tk()
    label = tk.Label(master, width=128, height=128, image=os.path.join(PIC_PATH, "idle.png"))
    label.pack()
    master.mainloop()

if __name__ == '__main__':
    main()