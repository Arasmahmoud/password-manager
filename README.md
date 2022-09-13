# password-manager

Password manager A program written in Python used to create strong passwords according to your desire, and it is saved in a text file, and there is the possibility of encrypting the file using Python so that it is not stolen


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


Password manager
برنامج مكتوب بلغة Python يستخدم لإنشاء كلمات مرور قوية حسب رغبتك ، ويتم حفظها في ملف نصي ، وهناك إمكانية لتشفير الملف باستخدام Python حتى لا يتم سرقتها

    كيف تستعمل :

    تحتاج إلى تثبيت بعض المكتبات: tkinter ، تشفير ، عشوائي (تشفير تثبيت pip3) (تثبيت pip3 tk) (تثبيت نقطة عشوائية)

    لإنشاء كلمة مرور وحفظها ، ما عليك سوى فتح passwd_manag.py وضع اسم الوسائط الاجتماعية في مربع intery والنقر فوق إنشاء كلمة مرور لإنشاء كلمة مرور وحفظها في ملف paask.txt مثل (facebook ==>> GHfgh ^٪ & 567hgh)

    إذا كنت تريد تشفير ملف paask.txt الخاص بك ، افتح en_de_code.py وانقر فوق تشفير المرور

    إذا كنت تريد dencrypt ملف paask.txt الخاص بك ، افتح en_de_code.py وانقر فوق dencrypt pass

    إذا كنت تريد الحصول على مفتاح تشفير ، فقط افتح en_de_code.py باستخدام أي محرر نصوص سترى full_kay = ("المفتاح هنا")

    إذا كنت تريد رؤية نص واضح لكلمة المرور ، فما عليك سوى تشغيل en_de_code.py والنقر فوق dencrypt pass بعد أن تتمكن من فتح paask.txt أو تشغيل passwd_manag.py والنقر فوق إظهار المرور والحصول على المرور

    إذا كنت تريد إنشاء مفتاحك فهو سهل:
     from cryptography.fernet import Fernet
             key = Fernet.generate_key()
             print (key)

    ووضع مفتاحك في en_de_code.py ==> full_kay = ("ضع هنا")

    شكرا واستمتع مع ALM TECH (اراس محمود)



- thanks and enjoy BY ALM TECH ( ARAS MAHMOUD )
- github = Arasmahmoud
- nstagram = almcompany6
- facebook = Almcompany6
- twitter = araskurdi0
