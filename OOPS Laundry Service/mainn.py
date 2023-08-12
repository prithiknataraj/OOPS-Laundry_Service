from tkinter import *
from csv import *
import reg
import loginscreen
import allocation
import report
from PIL import ImageTk, Image

'''with open("register.csv" , 'w') as reg:
    reg.truncate()
    reg.close()'''


'''class registerscrn:
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

        
        


        

        self.button=Button(self.root, text='Submit',width=20,bg='brown',fg='black')
        self.button.place(x=180,y=400)
        
        self.root.mainloop()

        
        
        
#rs=registerscrn()
#rs.register()'''

class mainscr:
 
    def screen(self):
        self.mainscreen = Tk()
        self.mainscreen.geometry('500x500')
        self.mainscreen.resizable(0, 0)
        self.mainscreen.title("MAIN")
        
        self.bg_frame = Image.open('/Users/mac/Downloads/oops.png')
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.mainscreen, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.place(width=500,height=500)
        #img1 = ImageTk.PhotoImage(Image.open("/Users/mac/Downloads/ssn laundry.jpeg"))
        #labelssn = Label(mainscreen, image = img1)
        #labelssn.pack()
        def registrationscr():
            self.mainscreen.destroy()
            rs=reg.registerscrn()
            rs.register()
            
        def lgscr():
            self.mainscreen.destroy()
            rs=loginscreen.login_screen()
            rs.login()
            
        def allocationscreen():
            a=allocation.Allocation()
            a.allocate()

        def reportscreen():
            r=report.Report()
            r.reportt()
            
        self.registerbutton= Button(self.mainscreen, text='REGISTER', font=("gotham", 16, "bold"), width=10,height=1, bd=0,fg='red',bg='black',highlightbackground="black",command=registrationscr)
        self.registerbutton.place(x=57,y=272)

        self.loginbutton= Button(self.mainscreen, text='ORDER', font=("gotham", 16, "bold"), width=10,height=1, bd=0,fg='red',bg='black',command=lgscr)
        self.loginbutton.place(x=290,y=272)

        self.servicepointbutton= Button(self.mainscreen, text='SERVICE POINT', font=("gotham", 16, "bold"), width=12,height=1, bd=0,fg='red',bg='black',command=allocationscreen)
        self.servicepointbutton.place(x=45,y=370)

        self.reportbutton= Button(self.mainscreen, text='REPORT', font=("gotham", 16, "bold"), width=10,height=1, bd=0,fg='red',bg='black',command=reportscreen)
        self.reportbutton.place(x=290,y=370)

        
        '''self.orderbutton= Button(self.mainscreen, text='ORDER', font=("gotham", 16, "bold"), width=22,height=2, bd=0,fg='red',bg='black')
        self.orderbutton.place(x=120,y=300)'''
    

ms=mainscr()
ms.screen()
