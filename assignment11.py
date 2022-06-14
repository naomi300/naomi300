#creating a digital clock

import time

from tkinter import*
window = Tk()
window.title("digital clock")
window.geometry("350x200")
window.resizable(1,1)
label =Label(window, font=("New times Roman", 30, "bold"), bg="blue",fg="white",bd= 30)
label.grid(row=0,column=1)
def digitalclock():
    text_input = time.strftime("%H:%M:%S")
    label.configure (text=text_input)
    label.after(200, digitalclock)
digitalclock()
window.mainloop()







