from tkinter import *
import transaction_slip
from csv import *
from calendar import *
from datetime import *

class Report:
    
    def reportt(self):
        root = Tk()
        report_list=[]
        
        with open("report.csv","r") as f:
            a=reader(f)
            for i in a:
                if i != []:
                    report_list.append(i)
        f.close()
                
        lst1=[]#list for reg id
        lst2=[] #list for price
        
        for i in report_list:
            lst1.append(int(i[0]))
            lst2.append(int(i[1]))

        lst2_tot = sum(lst2)#total price
        lst1_tot=len(lst1)#total no of ppl

        present_date = date.today()                   #present date.
        present_day = present_date.isoweekday()       #present day.
        temp = []

        with open("date.csv",'r') as day:
            previous_day = reader(day)
            for i in previous_day:
                if i != []:
                    temp.append(i)
            day.close()
                    
        pre_day = temp[0][0]

        #**********************************condition for daily report********************************

        if pre_day != present_day:
            l=[]
            l.append(pre_day)

            #to delete the values of report file.
            with open("date.csv","w") as f:
                f.truncate()
                write = writer(f)
                write.writerow(l)
            f.close()

            #to append the total cost daily.
            report_list.clear()
            report_list.append(lst2_tot)
                           
            with open("daily.csv",'a') as f1:
                write = writer(f1)
                write.writerow(report_list)
            f1.close()
        

        report_label = Label(root , text = "Report\n" , font = ("Bradley Hand ITC" , 40 , "bold" , "italic") , fg = "red")
        heading_label = Label(root , text = "Register number " + (2 * "\t") + "Price", font = ("Bradley Hand ITC" , 25 , "bold" , "italic"), fg="blue" , bg="white")


        report_label.pack()
        heading_label.pack(fill=X)

        for i in range(len(lst1)):
            a ,b = str(lst1[i]) , str(lst2[i])

            if i%2 != 0:
                x_label = Label(root , text = a + (5 * "\t") + b , font = ("Bradley Hand ITC" , 15) , bg = "white")

            else:
                x_label = Label(root , text = a + (5 * "\t") + b , font = ("Bradley Hand ITC" , 15) )
            x_label.pack(fill=X)

        total_label1 = Label(root , text = "Total no. of customers : " + str(lst1_tot) , font = ("Bradley Hand ITC" , 25))
        total_label2 = Label(root , text = "Total Price : " + str(lst2_tot) , font = ("Bradley Hand ITC" , 25))


        total_label1.pack()
        total_label2.pack()

        root.title("Report")
        root.mainloop()

'''l = [2]
with open("date.csv",'w') as f:
    write = writer(f)
    write.writerow(l)
R = Report()
R.reportt()'''

