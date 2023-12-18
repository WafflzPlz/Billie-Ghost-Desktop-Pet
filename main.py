import tkinter as tk
import os
from dotenv import load_dotenv
from PIL import ImageTk, Image

load_dotenv()
PIC_PATH = os.getenv("PIC_PATH")

def main():
    root = tk.Tk()
    root.geometry("128x128")
    #root.config(bg="#00008b")
    #root.wm_attributes("-transparentcolor", "#0000b8")
    root.overrideredirect(True)


    img = Image.open(os.path.join(PIC_PATH, "idle.png"))
    img = img.resize((128, 128), Image.NEAREST)
    img = ImageTk.PhotoImage(img)
    #img = tk.PhotoImage(file=os.path.join(PIC_PATH, "idle.png"))

    label = tk.Label(image=img)
    label.pack()

    #root.wait_visibility(root)
    #root.wm_attributes("-alpha", 0.5)
    root.mainloop()

if __name__ == '__main__':
    main()