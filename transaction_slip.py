from tkinter import *
from csv import *
import testq

class Trans_id:

    def __init__(self):
        
    
        self.details,templist = [],[]
        a , b , c = 0 , 0 , 0

        

        with open("details.csv" , 'r') as det:
            read = reader(det)

            for i in read:
                if "user" in i:
                    user_details = i[1:]
                    
                if "wash" in i:
                    l = list(int(j) for j in i[1:])
                    self.details.insert(0 , l)
                    a = 1

                if "iron" in i:
                    l = list(int(j) for j in i[1:])
                    self.details.insert(1 , l)
                    b = 1

                if "wash and iron" in i:
                    l = list(int(j) for j in i[1:])
                    self.details.insert(2 , l)
                    c = 1

        det.close()

        

        self.name = user_details[0]
        self.department = user_details[2]
        self.ph = user_details[3]
        self.id = user_details[4]
        

        if a == 0:
            self.details.insert(0 , [0,0,0])

        if b == 0:
            self.details.insert(1 , [0,0,0])

        if c == 0:
            self.details.insert(2 , [0,0,0])
            
        w = sum(self.details[0])
        i = sum(self.details[1])
        wi = sum(self.details[2])


        
        self.ncw = w + wi
        self.nci = i + wi
        self.tnc = self.ncw + self.nci

        self.wc = self.ncw * 7
        self.ic = self.nci * 7
        self.tc = self.wc + self.ic

        templist.append(self.id)
        templist.append(self.tc)
        with open("report.csv","a") as f:
            write=writer(f)
            write.writerow(templist)
        f.close()
        
        self.sncw = str(self.ncw)
        self.snci = str(self.nci)
        self.stnc = str(self.tnc)
        self.swc = str(self.wc)
        self.sic = str(self.ic)
        self.stc = str(self.tc)

        

    def slip(self):
        root = Tk()
        
        #---------------------title label--------------------
        Title = Label(root , text = "OOPS!\nLaundry Service" , font = ("Bradley Hand ITC" , 35 , "bold" , "italic") , fg = "red")
        sub_title = Label(root , text = "Transaction Slip\n" , font = ("Bradley Hand ITC" , 15) , fg = "brown")

        #--------------------slip details--------------------
        id_label = Label(root , text = "Customer ID : " + self.id , font = ("Bradley Hand ITC" , 20) , fg = "black" , bg = "white")
        name_label = Label(root , text = "Name : " + self.name , font = ("Bradley Hand ITC" , 20) , fg = "black")
        dip_label = Label(root , text = "Department : " + self.department , font = ("Bradley Hand ITC" , 20) , fg = "black" , bg = "white")
        ph_label = Label(root , text = "Phone Number : " + self.ph , font = ("Bradley Hand ITC" , 20) , fg = "black")
        ncw_label = Label(root , text = "Number of Clothes for washing : " + self.sncw , font = ("Bradley Hand ITC" , 20) , fg = "black" , bg = "white")
        nci_label = Label(root , text = "Number of clothes for ironing : " + self.snci , font = ("Bradley Hand ITC" , 20) , fg = "black")
        tnc_label = Label(root , text = "Total number of clothes : " + self.stnc , font = ("Bradley Hand ITC" , 20) , fg = "black" , bg = "white")
        wc_label = Label(root , text = "Cost of washing " + self.sncw + " clothes : " + self.swc , font = ("Bradley Hand ITC" , 20) , fg = "black")
        ic_label = Label(root , text = "Cost of ironing " + self.snci + " clothes : " + self.sic , font = ("Bradley Hand ITC" , 20) , fg = "black" , bg = "white")
        tc_label = Label(root , text = "Total Cost : " + self.stc , font = ("Bradley Hand ITC" , 25 , "bold") , fg = "black")

        #---------------------positioning--------------------
        Title.pack(fill = X)
        sub_title.pack(fill = X)

        id_label.pack(fill = X)
        name_label.pack(fill = X)
        dip_label.pack(fill = X)
        ph_label.pack(fill = X)
        ncw_label.pack(fill = X)
        nci_label.pack(fill = X)
        tnc_label.pack(fill = X)
        wc_label.pack(fill = X)
        ic_label.pack(fill = X)
        tc_label.pack(fill = X)

        root.title("Transaction Slip")                   #window title
        root.geometry("600x700")
        root.mainloop()
