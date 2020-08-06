from tkinter import *
root=Tk()

def click(event):
	text=event.widget.cget("text")
	if text=="=":
		if scvalue.get().isdigit():
			value=int(scvalue.get())
		else:
			try:
				value=eval(scvalue.get())
			except Exception as e:
				print(e)
				value="Error"
		scvalue.set(value)
		screen.update()
	elif text=="c":
		scvalue.set("")
		screen.update()
	elif text=="x":
		a=scvalue.get()
		scvalue.set(a[:-1])
		screen.update()
	else:
		scvalue.set(scvalue.get()+text)
		screen.update()

root.geometry("330x510")
root.minsize(width=320,height=510)
root.maxsize(width=320,height=510)
root.title("Calculator")
scvalue=StringVar()
scvalue.set("")
root.wm_iconbitmap("tut26i.ico")
screen=Entry(root, textvar=scvalue, font="lucida 25 bold")
screen.pack(fill=X, ipadx=9, pady=10,padx=10)

f=Frame(root, bg="grey")
f.pack()
b=Button(f, text="9",padx=28,pady=12,font="sansserif 15 bold")
b.pack(side=LEFT,padx=4,pady=4)
b.bind("<Button-1>",click)
b=Button(f, text="8",padx=28,pady=12,font="sansserif 15 bold")
b.pack(side=LEFT,padx=4,pady=4)
b.bind("<Button-1>",click)
b=Button(f, text="7",padx=28,pady=12,font="sansserif 15 bold")
b.pack(side=LEFT,padx=4,pady=4)
b.bind("<Button-1>",click)

f=Frame(root, bg="grey")
f.pack()
b=Button(f, text="6",padx=28,pady=12,font="sansserif 15 bold")
b.pack(side=LEFT,padx=4,pady=4)
b.bind("<Button-1>",click)
b=Button(f, text="5",padx=28,pady=12,font="sansserif 15 bold")
b.pack(side=LEFT,padx=4,pady=4)
b.bind("<Button-1>",click)
b=Button(f, text="4",padx=28,pady=12,font="sansserif 15 bold")
b.pack(side=LEFT,padx=4,pady=4)
b.bind("<Button-1>",click)

f=Frame(root, bg="grey")
f.pack()
b=Button(f, text="3",padx=28,pady=12,font="sansserif 15 bold")
b.pack(side=LEFT,padx=4,pady=4)
b.bind("<Button-1>",click)
b=Button(f, text="2",padx=28,pady=12,font="sansserif 15 bold")
b.pack(side=LEFT,padx=4,pady=4)
b.bind("<Button-1>",click)
b=Button(f, text="1",padx=28,pady=12,font="sansserif 15 bold")
b.pack(side=LEFT,padx=4,pady=4)
b.bind("<Button-1>",click)

f=Frame(root, bg="grey")
f.pack()
b=Button(f, text="+",padx=28,pady=12,font="sansserif 15 bold")
b.pack(side=LEFT,padx=4,pady=4)
b.bind("<Button-1>",click)
b=Button(f, text="0",padx=28,pady=12,font="sansserif 15 bold")
b.pack(side=LEFT,padx=4,pady=4)
b.bind("<Button-1>",click)
b=Button(f, text="*",padx=28,pady=12,font="sansserif 15 bold")
b.pack(side=LEFT,padx=4,pady=4)
b.bind("<Button-1>",click)

f=Frame(root, bg="grey")
f.pack()
b=Button(f, text="-",padx=29,pady=12,font="sansserif 15 bold")
b.pack(side=LEFT,padx=4,pady=4)
b.bind("<Button-1>",click)
b=Button(f, text="/",padx=29,pady=12,font="sansserif 15 bold")
b.pack(side=LEFT,padx=4,pady=4)
b.bind("<Button-1>",click)
b=Button(f, text="=",padx=29,pady=12,font="sansserif 15 bold")
b.pack(side=LEFT,padx=4,pady=4)
b.bind("<Button-1>",click)

f=Frame(root, bg="grey")
f.pack()
b=Button(f, text="c",padx=26,pady=12,font="sansserif 15 bold")
b.pack(side=LEFT,padx=5,pady=4)
b.bind("<Button-1>",click)
b=Button(f, text="%",padx=26,pady=12,font="sansserif 15 bold")
b.pack(side=LEFT,padx=5,pady=4)
b.bind("<Button-1>",click)
b=Button(f, text="x",padx=26,pady=12,font="sansserif 15 bold")
b.pack(side=LEFT,padx=5,pady=4)
b.bind("<Button-1>",click)






root.mainloop()
