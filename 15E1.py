from tkinter import *
import random
from PIL import Image, ImageTk

root = Tk()
root.title("Dice roll")

panel = Label(root, image = ImageTk.PhotoImage(Image.open("1.png")))

def roll():
    result = random.randint(1,6)
    file = str(result)+".png"
    img = ImageTk.PhotoImage(Image.open(file))
    panel = Label(root, image = img)

    
button = Button(root,
    text="Roll a dice",
    width=15,
    height=3,
    font = ("Times", 20, "bold"),
    bg="red",   # the color is changing with the presence of a pointer
    fg="white",
    command=roll,
)
button.pack()

panel.pack(side = "bottom", fill = "both", expand = "yes")


root.mainloop()
