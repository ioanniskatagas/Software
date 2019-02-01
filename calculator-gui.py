#import GUI window
from tkinter import *
window = Tk()
window.title("MooseTek Calculator GUI")
window.geometry('500x900')

#9
btn = Button(window, text="9")
btn.grid(column=0, row=0)

#8
btn2 = Button(window, text="8")
btn2.grid(column=1, row=0)

#7
btn3 = Button(window, text="7")
btn3.grid(column=2, row =0)

#+
btn4 = Button(window, text="+")
btn4.grid(column=3, row=0)

#6
btn5 = Button(window, text="6")
btn5.grid(column=0, row=1)

#5
btn6 = Button(window, text="5")
btn6.grid(column=1, row=1)

#4
btn7 = Button(window, text="4")
btn7.grid(column=2, row=1)

#-
btn8 = Button(window, text="-")
btn8.grid(column=3, row=1)

#3
btn9 = Button(window, text="3")
btn9.grid(column=0, row=2)

#2
btn10 = Button(window, text="2")
btn10.grid(column=1, row=2)

#1
btn11 = Button(window, text="1")
btn11.grid(column=2, row=2)

#X
btn12 = Button(window, text="X")
btn12.grid(column=3, row=2)

#=
btn13 = Button(window, text="=")
btn13.grid(column=0, row=3)

#/
btn14 = Button(window, text="/")
btn14.grid(column=3, row=3)
