from tkinter import *
import random
from PIL import Image, ImageTk

root = Tk()
root.title("Dice roll")

def roll():
    result = random.randint(1,6)
    file = str(result)+".png"
    img = ImageTk.PhotoImage(Image.open(file))
    label = Label(root, image = img)
    label.image = img
    label.grid(row = 1)
    
button = Button(root,
    text="Roll a dice",
    width=15,
    height=3,
    font = ("Times", 20, "bold"),
    bg="red",   # the color is changing with the presence of a pointer
    fg="white",
    command=roll,
)

button.grid(row = 2)

root.mainloop()
