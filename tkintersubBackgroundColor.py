from tkinter import Tk,Label,RIGHT

root = Tk()
label1 = Label(root,text="Welcome to python",background="red")
label2 = Label(root,text="Have a Good day",background="green")
label1.pack(fill="y",padx=10,ipady=25,side=RIGHT)
label2.pack(fill="y",padx=20,ipady=40,side=RIGHT)
root.mainloop()