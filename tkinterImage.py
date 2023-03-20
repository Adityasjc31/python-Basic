from tkinter import Tk,Label,PhotoImage
import os
root = Tk()
img = PhotoImage(file=os.getcwd()+("\\R.jpg"))
IMG = Label(root,image=img)
IMG.pack()
root.mainloop()