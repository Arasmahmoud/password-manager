from random import choice 
from tkinter import *
from tkinter import ttk
from glas import fall

######################################
# written by ARAS MAHMOUD (ALM TECH) #
# instagram = almcompany6    	     #
# facebook = Almcompany6             #
######################################

root = Tk()
root.geometry("800x450+280+100")
root.title("ALM TECH")
root.resizable('false' , 'false')
root.config(bg='black')

l1 = Label(root, text="PASSWORD GENERATOR ", fg='gold', bg='black', font=('tajawal', '14', 'bold'))
l1.place(relx=0.5, rely=0.2, anchor=CENTER)

op =[8,10,12,22,24,26,28,30]
drop =ttk.Combobox(root,values=op)
drop.current(0)
drop.config(foreground="red",font=('tajawal','10','bold'))
drop.place(relx=0.5, rely=0.4, anchor=CENTER)

l2 = Label(root, text="Social Media name : ", fg='gold', bg='black', font=('tajawal', '12', 'bold'))
l2.place(relx=0.2, rely=0.8, anchor=CENTER)




name = StringVar()
textbox = Entry(root,fg="red",width=35,font=('tajawal', '14',"bold"),textvariable=name)
textbox.place(relx=0.6, rely=0.8, anchor=CENTER)


def full_password():
	sm =textbox.get()
	size = drop.get()
	size =int(size)
	passk = ""
	pass1 ="0Z9M4N6&CB@V2X21q9w!e7rty?u0i#op2asPOI4UY8T7R36E2W<Qdf5ghj4kl738z0xc4vbn>m9LK2JH/G6F3DSA"
	for nums in range(size):
		passk += choice(pass1)
		name.set(passk)
	ww = open("paask.txt","a")
	ww.write(sm+" ==> "+passk+"\n")
	ww.close()
	
	return passk	
	
def new ():
	root.destroy()
	fall()


b1 = Button(root, text='GENERATE', command=full_password, width=8, height=2, fg='gold', bg='red',font=('tajawal', '14', 'bold'))
b1.place(relx=0.7, rely=0.6, anchor=CENTER)

b8 = Button(root, text='Showpass', command=new, width=8, height=2, fg='gold', bg='red',font=('tajawal', '14', 'bold'))
b8.place(relx=0.3, rely=0.6, anchor=CENTER)






root.mainloop()


