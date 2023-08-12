from tkinter import *
from csv import *
import orderr

class wi__s:
    
    def wash_ironscreen(self):
        self.root4 = Tk()
        self.root4.geometry('500x500')
        
        self.root4.title("Placing order")
        self.label_1 = Label(self.root4, text="WASHING & IRONING",width=20,font=("bold", 20))
        self.label_1.place(x=90,y=65)

        self.label_2 = Label(self.root4, text="No of shirts",width=20,font=("bold", 10))
        self.label_2.place(x=70,y=170)

        self.entry_2 = Entry(self.root4)
        self.entry_2.place(x=240,y=170)

        self.label_3 = Label(self.root4, text="No of pants",width=20,font=("bold", 10))
        self.label_3.place(x=70,y=250)

        self.entry_3 = Entry(self.root4)
        self.entry_3.place(x=240,y=250)

        self.label_4 = Label(self.root4, text="No of bedspreads",width=20,font=("bold", 10))
        self.label_4.place(x=70,y=330)
        
        self.entry_4 = Entry(self.root4)
        self.entry_4.place(x=240,y=330)

        def wash_iron_cloths():
            #This function gets the details from the user and stores.
            ns = self.entry_2.get()
            np = self.entry_3.get()
            nb = self.entry_4.get()

            a = 0

            if (len(ns) > 0 and ns.isdigit() is not True) and a == 0:
                a == 1
                error = Label(self.root4 ,text = "invalid input!" , fg = "red")
                error.place(x = 220 , y = 440)

            elif len(np) > 0 and np.isdigit() is not True and a == 0:
                a == 1
                error = Label(self.root4 ,text = "invalid input!" , fg = "red")
                error.place(x = 220 , y = 440)

            elif len(nb) > 0 and nb.isdigit() is not True and a == 0:
                a == 1
                error = Label(self.root4 ,text = "invalid input!" , fg = "red")
                error.place(x = 220 , y = 440)

            else:

                if ns == '':
                    ns = 0

                else:
                    ns = int(ns)

                if np == '':
                    np = 0

                else:
                    np = int(np)

                if nb == '':
                    nb = 0

                else:
                    nb = int(nb)

                backfn4()          #to close the window.

                self.wash_iron = []

                self.wash_iron.append("wash and iron")
                self.wash_iron.append(ns)
                self.wash_iron.append(np)
                self.wash_iron.append(nb)

                with open("details.csv" , 'a') as det:
                    write = writer(det)
                    write.writerow(self.wash_iron)
                det.close()
        def backfn4():
            self.root4.destroy()
            gg=orderr.orderscr()
            gg.ord()
        self.button=Button(self.root4, text='back',width=20,bg='brown',fg='black',command=backfn4)
        self.button.place(x=270,y=395)
        self.button33=Button(self.root4, text='submit',width=20,bg='brown',fg='black' , command = wash_iron_cloths)
        self.button33.place(x=110,y=395)


        
        
    


