from random import choice 
from tkinter import *
from tkinter import ttk
import time 


######################################
# written by ARAS MAHMOUD (ALM TECH) #
# instagram = almcompany6    	     #
# facebook = Almcompany6             #
######################################

def fall():
	root = Tk()
	root.geometry("800x600+280+100")
	root.title("ALM TECH")
	root.resizable('false' , 'false')
	root.config(bg='black')


	##this well work after check uosername and password ##
	def auth():

		def getpass():
			r = open("paask.txt","r")
			all = r.read()
			r.close()
			alll = StringVar()
			alll.set(all)
			l2.config(textvariable=alll)
			l1.config(text="password is clear text")

		l1 = Label(root, text="PASSWORD SHOW ", fg='gold', bg='black', font=('tajawal', '14', 'bold'))
		l1.place(relx=0.5, rely=0.1, anchor=CENTER)

		l2 = Label(root, text="", fg='green', bg='black', font=('tajawal', '10', 'bold'))
		l2.place(relx=0.5, rely=0.6, anchor=CENTER)

		b1 = Button(root, text='GetPass', command=getpass, width=8, height=2, fg='gold', bg='red',font=('tajawal', '14', 'bold'))
		b1.place(relx=0.2, rely=0.1, anchor=CENTER)

	auth()
	root.mainloop()


