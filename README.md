# password-manager

Password manager A program written in Python used to create strong passwords according to your desire, and it is saved in a text file, and there is the possibility of encrypting the file using Python so that it is not stolen Have fun


- how to use :
- you need install some library : tkinter , cryptography , random  ( pip3 install cryptography )( pip3 install tk )( pip install random )
- to generate password and saved just open passwd_manag.py put social media name in intery box
 and click generate its will generate password and saved in paask.txt file like ( facebook ==> >GHfgh^%&567hgh )
- if you want encrypt your paask.txt file open en_de_code.py and click encrypt pass
- if you want dencrypt your paask.txt file open en_de_code.py and click dencrypt pass
- if want get encrypt key just open en_de_code.py with any text editor you will see full_kay = (" the key is here ")
- if you want see your password clear text just run en_de_code.py and click dencrypt pass after you can open paask.txt or run passwd_manag.py and click show pass and get pass 

- if want generate your key its easy :
             from cryptography.fernet import Fernet
             key = Fernet.generate_key()
             print (key)
             
- and put your key in en_de_code.py ==> full_kay = (" put here  ") 


- thanks and enjoy BY ALM TECH ( ARAS MAHMOUD )
- github = Arasmahmoud
- nstagram = almcompany6
- facebook = Almcompany6
- twitter = araskurdi0
