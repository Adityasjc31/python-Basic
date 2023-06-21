import re
from tkinter import *
from tkinter import messagebox
root = Tk()
root.attributes("-topmost", 1)
root.resizable(0, 0)
frameinput = Frame(root, height=40, width=50)
frameButton = Frame(root, height=240, width=210)
frameinput.pack(ipady=5)
frameButton.pack()
inputtext = StringVar()

def equals():
    print(inputtext.get())
    inputtext.set(eval(inputtext.get()))


def click(item):
    if item == "+":
        inputtext.set(inputtext.get()+"+")
    elif item == "-":
        inputtext.set(inputtext.get()+"-")
    elif item == "*":
        inputtext.set(inputtext.get()+"*")
    elif item == "/":
        inputtext.set(inputtext.get()+"/")
    elif item == "=":
        equals()
    elif item == "CLR":
        inputtext.set("")
    elif item == "0":
        inputtext.set(inputtext.get()+"0")
    elif item == "1":
        inputtext.set(inputtext.get()+"1")
    elif item == "2":
        inputtext.set(inputtext.get()+"2")
    elif item == "3":
        inputtext.set(inputtext.get()+"3")
    elif item == "4":
        inputtext.set(inputtext.get()+"4")
    elif item == "5":
        inputtext.set(inputtext.get()+"5")
    elif item == "6":
        inputtext.set(inputtext.get()+"6")
    elif item == "7":
        inputtext.set(inputtext.get()+"7")
    elif item == "8":
        inputtext.set(inputtext.get()+"8")
    elif item == "9":
        inputtext.set(inputtext.get()+"9")


Entry(frameinput, textvariable=inputtext, width=30, border=7, bg="white",
      justify="right", font=("Arial", 20, "bold"), state="readonly").grid(row=0, ipady=10)
Button(frameButton, text="7", padx=45, pady=15,
       command=lambda: click("7")).grid(row=1, column=0)
Button(frameButton, text="8", padx=45, pady=15,
       command=lambda: click("8")).grid(row=1, column=1)
Button(frameButton, text="9", padx=45, pady=15,
       command=lambda: click("9")).grid(row=1, column=2)
Button(frameButton, text="+", padx=43.5, pady=15,
       command=lambda: click("+")).grid(row=1, column=3)
Button(frameButton, text="4", padx=45, pady=15,
       command=lambda: click("4")).grid(row=2, column=0)
Button(frameButton, text="5", padx=45, pady=15,
       command=lambda: click("5")).grid(row=2, column=1)
Button(frameButton, text="6", padx=45, pady=15,
       command=lambda: click("6")).grid(row=2, column=2)
Button(frameButton, text="-", padx=45, pady=15,
       command=lambda: click("-")).grid(row=2, column=3)
Button(frameButton, text="1", padx=45, pady=15,
       command=lambda: click("1")).grid(row=3, column=0)
Button(frameButton, text="2", padx=45, pady=15,
       command=lambda: click("2")).grid(row=3, column=1)
Button(frameButton, text="3", padx=45, pady=15,
       command=lambda: click("3")).grid(row=3, column=2)
Button(frameButton, text="*", padx=45, pady=15,
       command=lambda: click("*")).grid(row=3, column=3)
Button(frameButton, text="0", padx=45, pady=15,
       command=lambda: click("0")).grid(row=4, column=0)
Button(frameButton, text="CLR", padx=38, pady=15,
       command=lambda: click("CLR")).grid(row=4, column=1)
Button(frameButton, text="=", padx=45, pady=15,
       command=lambda: click("=")).grid(row=4, column=2)
Button(frameButton, text="/", padx=45, pady=15,
       command=lambda: click("/")).grid(row=4, column=3)

root.mainloop()
