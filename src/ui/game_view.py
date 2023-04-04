from tkinter import *

win = Tk()
win.geometry("900x450")

def create_label(n):
    labels = []
    for i in range(1, n+1):
        label = Label(win,
            height= 2,
            width=6,
            text=str(i),
            font=("Helvetica", 25),
            foreground="white",
            background="blue")
        labels.append(label)
    return labels

labels = create_label(5)

for label in labels:
    label.pack(side=LEFT,
               padx=15)

win.mainloop()