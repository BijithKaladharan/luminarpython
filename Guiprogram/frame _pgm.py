from tkinter import*

root=Tk()
tFrame=Frame(root)
bFrame=Frame(root)

tFrame.pack()
bFrame.pack(side=BOTTOM)

btn1=Button(tFrame,text="FirstButton",fg="green")
btn2=Button(tFrame,text="SecondButton",fg="blue")
btn3=Button(tFrame,text="ThirdButton",fg="red")
btn4=Button(tFrame,text="FourthButton",fg="black")
btn1.pack(side=LEFT)
btn2.pack(side=LEFT)
btn3.pack(side=LEFT)
btn4.pack(side=BOTTOM)

root.mainloop()