from tkinter import Tk,Message

root = Tk()
msg = Message(root,text="Welcome to GUI")
msg.config(font=('calibri',24,'italic bold underline'))
msg.pack()
root.mainloop()