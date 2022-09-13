from tkinter import *
from tkinter import ttk
import time 
from cryptography.fernet import Fernet 


#################################################################
#					written by ARAS MAHMOUD	(ALM TECH)			#
#					instagram = almcompany6 		            #
#					facebook = Almcompany6                      #
#################################################################


root = Tk()
root.geometry("400x200+280+100")
root.title("ALM TECH EN//DE")
root.resizable('false' , 'false')
root.config(bg='black')



def decrypt():
	full_kay = '4oZTMSYb1xiEp2z0gJ8yz4iceWz-evLWlm-hqyThI2w='
	file_txt = open("paask.txt","rb")
	file_txt2 = file_txt.read()
	file_txt = open("paask.txt","wb")
	en = Fernet(full_kay).decrypt(file_txt2)
	file_txt.write(en)
	file_txt.close()
	de1['state'] = 'disabled'


def encrypt():
	full_kay1 = '4oZTMSYb1xiEp2z0gJ8yz4iceWz-evLWlm-hqyThI2w='

	file_txt1 = open("paask.txt","rb")
	file_txt21 = file_txt1.read()
	file_txt1 = open("paask.txt","wb")
	en = Fernet(full_kay1).encrypt(file_txt21)
	file_txt1.write(en)
	file_txt1.close()
	en1['state'] = 'disabled'








en1 = Button(root, text='EncodePass',command=encrypt ,width=8, height=2, fg='gold', bg='red',font=('tajawal', '14', 'bold'))
en1.place(relx=0.5, rely=0.2, anchor=CENTER)

de1 = Button(root, text='DecodePass',command=decrypt ,width=8, height=2, fg='gold', bg='red',font=('tajawal', '14', 'bold'))
de1.place(relx=0.5, rely=0.6, anchor=CENTER)








root.mainloop()