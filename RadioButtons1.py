from tkinter import *

mw =Tk()
mw.title('vidya jyothi college')
mw.geometry('900x720')

#creating Freames
frame1 = LabelFrame(mw,text='This is frame1',font=('',14),width=400,padx=10, pady=10) #no use of width operator ,size will increase only based on widgets like buttons
frame1.grid(row=0,column=0,padx=10,pady=10)

exit_btn = Button(frame1, text='Exit!',padx=60,pady=12,font=('',14),command=mw.quit)
exit_btn.pack()

#creating radio buttons
#we want a func to be excuted when we select an option

def rbv_res():
    rbv_lbl.config(text=rbv.get())           # get() will fetch the value of rbv

rbv= IntVar()
Radiobutton(frame1,value=1, variable=rbv, text='option 1', font=('',14),command=rbv_res).pack(pady=(20,10))
#variable=rbv , value=1, we know that var=value ,so rbv=1
Radiobutton(frame1,value=2, variable=rbv, text='option 2', font=('',14),command=rbv_res).pack(pady=(0,20))
#variable=rbv , value=2, we know that var=value ,so rbv=2

rbv_lbl = Label(frame1, text='',font=('',14))
rbv_lbl.pack()

mw.mainloop()