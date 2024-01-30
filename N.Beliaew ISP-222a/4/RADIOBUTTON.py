from tkinter import *
def trace_func(var, index, mode):
    label.config(text=v.get())
def create_radiobutton(root, text, u):
    rb = Radiobutton(frame, text=text, value=u, indicatoron=0, width=20, height=3, variable=v)
    rb.pack()
root = Tk()
frame = Frame(root)
v = StringVar()
v.trace_add("write", trace_func)
u = {"Вася" : "+4 0000000000",
"Петя" : "+4 9087654321",
"Маша" : "+4 1111111111"}
for (text, phone) in u.items():
    create_radiobutton(frame, text, phone)
frame.pack(side=LEFT)
label = Label(root, text="", width=20)
label.pack(side=RIGHT, padx=10)
v.set(u["Петя"])
root.mainloop()
