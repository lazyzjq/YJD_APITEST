#coding=utf-8
import Tkinter as tk

windows=tk.Tk()
windows.title('the window')
windows.geometry('1000x800')
var=tk.StringVar()
on_hit=False
def hit_me():
    global on_hit
    if on_hit==False:
        on_hit=True
        var.set(u'你摁我干嘛')
    else:
        on_hit=False
        var.set('')
l=tk.Label(windows,
           textvariable=var,
           text='lable',
           bg='purple',
           font=('Arial',16),
           width=20,
           height=10)
l.pack()
b=tk.Button(windows,
            text='hit me',
            width=15,
            height=2,
            command=hit_me
            )
b.pack()

windows.mainloop()