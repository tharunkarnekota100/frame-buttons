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
#speciality of radio buttons it selects only one option from the all existing options
#pady=(x,y) : x is for top , y is for bottom

rbv= IntVar()        #rbv:radio button variable       #as rbv is a a tkinter varaiable it should be difined by its datatype format
Radiobutton(frame1,value=1, variable=rbv, text='option 1', font=('',14)).pack(pady=(20,10))
Radiobutton(frame1,value=2, variable=rbv, text='option 2', font=('',14)).pack(pady=(0,20))

mw.mainloop()