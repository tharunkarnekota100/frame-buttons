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

rbv= StringVar()
rbv.set('chicken biryani')
Radiobutton(frame1,value='chicken biryani', variable=rbv, text='option 1', font=('',14),command=rbv_res).pack(pady=(20,10))
#variable=rbv , value='chicken biryani', we know that var=value ,so rbv='chicken biryani'
Radiobutton(frame1,value='veg biryani', variable=rbv, text='option 2', font=('',14),command=rbv_res).pack(pady=(0,20))
#variable=rbv , value='veg biryani', we know that var=value ,so rbv='veg biryani'

rbv_lbl = Label(frame1, text=rbv.get(),font=('',14))
rbv_lbl.pack()


#create check button/boxs
def cbv_res():
    cbv_lbl.config(text=cbv.get())           # get() will fetch the value of rbv

cbv = StringVar()
cb = Checkbutton(frame1, onvalue='yes', offvalue='no', variable=cbv,text='Do you Want Parcle?',font=('',14),command=cbv_res)
cb.deselect()     #initally the button will be selected ,,by deselect() we make it unselected
cb.pack(pady=(30,10))

cbv1 = StringVar()
cb1 = Checkbutton(frame1, onvalue='yes', offvalue='no', variable=cbv1,text='Do you Want eat?',font=('',14),command=cbv_res)
cb1.deselect()     #initally the button will be selected ,,by deselect() we make it unselected
cb1.pack(pady=(30,10))

cbv_lbl = Label(frame1, text=cbv.get(),font=('',14))
cbv_lbl.pack(pady=(0,30))

#creating Drop Down Menus

selected=StringVar()
selected.set('March')
options= OptionMenu(frame1,selected,'january','february','march')
#varaiable is interrnally defined as 'selected' ie varaiable=selected
options.pack()

mw.mainloop()

#check buttons will work independently
#cb and cb1 are independent to eachother