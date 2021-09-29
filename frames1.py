from tkinter import *

mw =Tk()
mw.title('vidya jyothi college')
mw.geometry('900x720')

#creating Freames
#frames is like a window but it is part of window

frame1 = LabelFrame(mw,text='This is frame1',font=('',14),width=400,padx=10, pady=10) #no use of width operator ,size will increase only based on widgets like buttons
frame1.grid(row=0,column=0,padx=10,pady=10)

#it will only visible when it has some content

exit_btn = Button(frame1, text='Exit!',padx=60,pady=12,font=('',14),command=mw.quit)
exit_btn.pack()

mw.mainloop()