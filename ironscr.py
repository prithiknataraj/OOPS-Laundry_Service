from tkinter import *
from csv import *
import orderr

class i__s:
    
    def ironingscreen(self):
        self.root1 = Tk()
        self.root1.geometry('500x500')
        
        self.root1.title("Placing order")
        self.label_2 = Label(self.root1, text="IRONING",width=20,font=("bold", 20))
        self.label_2.place(x=90,y=65)

        self.label_3 = Label(self.root1, text="No of shirts",width=20,font=("bold", 10))
        self.label_3.place(x=70,y=170)

        self.entry_3 = Entry(self.root1)
        self.entry_3.place(x=240,y=170)

        self.label_4 = Label(self.root1, text="No of pants",width=20,font=("bold", 10))
        self.label_4.place(x=70,y=250)

        self.entry_4 = Entry(self.root1)
        self.entry_4.place(x=240,y=250)

        self.label_5 = Label(self.root1, text="No of bedspreads",width=20,font=("bold", 10))
        self.label_5.place(x=70,y=330)
        
        self.entry_5 = Entry(self.root1)
        self.entry_5.place(x=240,y=330)

        def iron_cloths():
            #This function gets the details from the user and stores.
            ns = self.entry_3.get()
            np = self.entry_4.get()
            nb = self.entry_5.get()

            a = 0

            if (len(ns) > 0 and ns.isdigit() is not True) and a == 0:
                a == 1
                error = Label(self.root1 ,text = "invalid input!" , fg = "red")
                error.place(x = 220 , y = 440)

            elif len(np) > 0 and np.isdigit() is not True and a == 0:
                a == 1
                error = Label(self.root1 ,text = "invalid input!" , fg = "red")
                error.place(x = 220 , y = 440)

            elif len(nb) > 0 and nb.isdigit() is not True and a == 0:
                a == 1
                error = Label(self.root1 ,text = "invalid input!" , fg = "red")
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

                backfn3()          #to close the window.

                self.iron = []

                self.iron.append("iron")
                self.iron.append(ns)
                self.iron.append(np)
                self.iron.append(nb)

                with open("details.csv" , 'a') as det:
                    write = writer(det)
                    write.writerow(self.iron)

                det.close()

            
        def backfn3():
            self.root1.destroy()
            gg=orderr.orderscr()
            gg.ord()
        self.button=Button(self.root1, text='back',width=20,bg='brown',fg='black',command=backfn3)
        self.button.place(x=270,y=395)

        self.button33=Button(self.root1, text='submit',width=20,bg='brown',fg='black' , command = iron_cloths)
        self.button33.place(x=110,y=395)

        
        
    
#b=i__s()
#b.ironingscreen()
