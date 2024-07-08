from tkinter import *
import mainn
from csv import *



class registerscrn:

    a , b , c , d , e = 0 , 0 , 0 , 0 , 0

    def backfn1(self):
            self.root.destroy()
            ms=mainn.mainscr()
            ms.screen()

    def store(self,lst):
        with open("register.csv","a") as reg_file:
            write=writer(reg_file)
            write.writerow(lst)
        reg_file.close()

    def getentry(self):
        lst=[]

        name = self.entry_1.get()
        lst.append(name)

        mail=self.entry_2.get()
        lst.append(mail)

        dept=self.entry_3.get()
        lst.append(dept)

        phoneno=self.entry_4.get()
        lst.append(phoneno)

        rollno=self.entry_5.get()
        lst.append(rollno)

        if '@' not in mail and self.e == 0 and len(mail) > 0:
            # condition for gmail.
            self.e = 1
            error = Label(self.root ,text = "invalid input!" , fg = "red")
            error.place(x = 380 , y = 180)

        if name.isalpha() is not True and len(name) > 0:
            # condition for name.
            if self.d == 0:
                self.d = 1
                error = Label(self.root ,text = "invalid input!" , fg = "red")
                error.place(x = 380 , y = 130)

        if len(phoneno) > 0 and (phoneno.isdigit() is not True or len(phoneno) != 10):
            # condition for phone number.
            if self.a == 0:
                self.a = 1
                error = Label(self.root ,text = "invalid input!" , fg = "red")
                error.place(x = 380 , y = 280)

        if  len(rollno) > 0 and(rollno.isdigit() is not True or len(rollno)!=7):
            #condition for rollno.
            if self.c == 0:
                self.c = 1
                error = Label(self.root ,text = "invalid input!" , fg = "red")
                error.place(x = 380 , y = 335)

        elif name == '' or mail == '' or dept == '' or phoneno == '' or rollno == '':
            # condition for empty input.
            if self.b == 0:
                self.b = 1
                error2 = Label(self.root ,text = "enter the edtails!" , fg = "red")
                error2.place(x = 220 , y = 450)

        else:

            self.store(lst)
            self.backfn1()
        

        
    def register(self):
    
        self.root = Tk()
        self.root.geometry('500x500')
        
        self.root.title("Registration Form")

        self.label_0 = Label(self.root, text="REGISTER",width=20,font=("bold", 20))
        self.label_0.place(x=90,y=53)


        self.label_1 = Label(self.root, text="Name",width=20,font=("bold", 10))
        self.label_1.place(x=70,y=130)

        self.entry_1 = Entry(self.root)
        self.entry_1.place(x=240,y=130)
        
        

        self.label_2 = Label(self.root, text="Email",width=20,font=("bold", 10))
        self.label_2.place(x=68,y=180)
        

        self.entry_2 = Entry(self.root)
        self.entry_2.place(x=240,y=180)
        

        self.label_3 = Label(self.root, text="Department",width=20,font=("bold", 10))
        self.label_3.place(x=70,y=230)
        self.entry_3 = Entry(self.root)
        self.entry_3.place(x=240,y=230)
        
        

        self.label_4 = Label(self.root, text="Phone Number",width=20,font=("bold", 10))
        self.label_4.place(x=70,y=280)


        self.entry_4 = Entry(self.root)
        self.entry_4.place(x=240,y=280)
        

        self.label_5 = Label(self.root, text="ROLL NO",width=20,font=("bold", 10))
        self.label_5.place(x=70,y=335)

        self.entry_5 = Entry(self.root)
        self.entry_5.place(x=240,y=335)
        
        self.button=Button(self.root, text='Submit',width=20,bg='brown',fg='black' , command = self.getentry)
        self.button.place(x=270,y=400)
        self.button22=Button(self.root, text='back',width=20,bg='brown',fg='black',command=self.backfn1)
        self.button22.place(x=105,y=400)
        
        self.root.mainloop()



        
        
        

