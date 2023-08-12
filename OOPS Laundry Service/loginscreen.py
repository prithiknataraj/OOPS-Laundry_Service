from tkinter import *
from csv import *
import mainn
import orderr

class login_screen:

    b = 0

    def getEntry(self):

        details_list = []
        
        def openorder():
            self.root7.destroy()
            o=orderr.orderscr()
            o.ord()

        #csv file
        with open("register.csv",'r') as reg_file:
            read = reader(reg_file)
            
            for i in read:
                
                if i != []:
                    details_list.append(i)

        login_id = self.entry_1.get()

        #test condition for opening the orderr window.
        if len(login_id) == 7:
            a = 0

            for i in details_list:
                
                if login_id == i[4]:

                    i.insert(0,"user")
                    with open("details.csv",'w') as det:
                        det.truncate()
                        write = writer(det)
                        write.writerow(i)          #contains the current user details.
                    det.close()
                    
                    a = 1
                    #closing login window and moving to orderr screen.
                    openorder()
                    
                    break

            if a == 0 and self.b == 0:
                Label(self.root7 , text = "Invalid User ID" , fg = "red").pack()
                self.b = 1

        else:
            if self.b == 0:
                Label(self.root7 , text = "Invalid User ID" , fg = "red").pack()
                self.b = 1
            
    
    def login(self):

        self.root7 = Tk()
        self.root7.geometry('500x500')
        
        self.root7.title("Login Form")
        def backfn():
           self.root7.destroy()
           ms=mainn.mainscr()
           ms.screen()
            

        self.label_0 = Label(self.root7, text="LOGIN",width=20,font=("bold", 20))
        self.label_0.place(x=90,y=53)


        self.label_1 = Label(self.root7, text="ROLL NO",width=20,font=("bold", 10))
        self.label_1.place(x=70,y=130)

        self.entry_1 = Entry(self.root7)
        self.entry_1.place(x=240,y=130)        
        
        self.button=Button(self.root7, text='login',width=20,bg='brown',fg='black',command=self.getEntry)
        self.button.place(x=270,y=200)
        
        self.button111=Button(self.root7, text='back',width=20,bg='brown',fg='black',command=backfn)
        self.button111.place(x=100,y=200)
        
        self.root7.mainloop()

    






