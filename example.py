#!/usr/bin/python
##########################
#            NAME:  Naomi Njeri
#            DATE:  07/06/2022
###########################


from cgitb import text
from struct import pack
from tkinter import*
window = Tk()
window.title("welcome to my awesome app")
window.configure(bg="blue")
window.geometry("400x600")

f_name = Label(window,text="first name",font=("Arial Bold",12))
s_name = Label(window,text="second name",font=("Arial Bold",12))

f_name.grid(column =60 ,row =100)
s_name.grid(column =60 ,row =120)

btn= Button(window,text="click me",bg="white",width=30,command=open_popup().pack())
btn.grid(column=100, row=150)

f_name_box=Entry(window,width=30)
s_name_box=Entry(window,width=30)

f_name_box.grid(column=100 ,row=100)
s_name_box.grid(column=100 ,row=120)

def open_popup():
    top = Toplevel(window)
    top.geometry("300x300")
    top.title("Pop up window")
    top.configure(bg="red")
    msg= Label(top,text="welcome to the Pop up".place (x=150,y=150))

window.mainloop()