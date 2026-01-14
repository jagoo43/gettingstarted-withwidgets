from tkinter import *
from datetime import date
root=Tk()
root.title("getting started with widgets")
root.geometry("400x300")
lbl=Label(text="hey there",fg="white",bg="#0072ff",height=1,width=300)
namelbl=Label(text="full name",bg="#9763D3",width=250)
nameentry=Entry()
def display():
    name=nameentry.get()
    global message
    message="welcome to the application \n todays date is:"
    greet = "hello"+name+"\n"
    text_box.insert(END,greet)
    text_box.insert(END,message)
    text_box.insert(END,date.today())
text_box=Text(height=3)
btn=Button(text="begin",command=display,height=1,bg="#0112ff",fg="white")
lbl.pack()
namelbl.pack()
nameentry.pack()
btn.pack()
text_box.pack()
root.mainloop()