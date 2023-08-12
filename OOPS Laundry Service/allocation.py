#M.Padhma Priya and R.Narmatha
#312215002074 and 3122215002069

import tkinter as tk
from tkinter import messagebox
from Qfunctions import PQueue

class Allocation:
    def allocate(self):
        
        #create a window with required title and geometry
        window=tk.Tk()
        #window['bg']='grey'
        window.title("ALLOCATION")
        window.geometry("550x450")

        label=tk.Label(window,text="CLICK TO ASSIGN",font=("Comic Sans MS", 10, "bold"))
        label.place(x=150,y=60)

        #object created for class PQueue as ts
        ts=PQueue()

        #get the input for register id to be enqueued
        e=tk.Entry(window,width=7)
        e.place(x=200,y=100)

        def func():
            try:
                int(e.get())
                ts.enqueue(str(e1.get()))
                answer.config(text="")
 
            except ValueError:
                answer.config(text="Enter a number!")

        answer=tk.Label(window,text="")
        answer.place(x=400,y=100)
        #create a button to call enqueue function when clicked
        button=tk.Button(window, text="ASSIGN",bg="black",fg="red",font=("gotham", 10, "bold"),command=func)
        button.place(x=300,y=100)

        label1=tk.Label(window,text="ENTER SERVICE POINT NUMBER",font=("Comic Sans MS", 10, "bold"))
        label1.place(x=150,y=160)


        #get the input for queue number from which id has to be dequeued
        e1=tk.Entry(window,width=1)
        e1.place(x=200,y=200)

        def func1():
            try:
                int(e.get())
                ts.dequeue(str(e1.get()))
                answer1.config(text="")
            except ValueError:
                answer1.config(text="Enter a number!")

        answer1=tk.Label(window,text="")
        answer1.place(x=450,y=200)  
                

        #create a button to call dequeue function
        button1=tk.Button(window, text="CLOSE TRANSACTION",fg="red",bg="black",font=("gotham", 10, "bold"),command=func1)
        button1.place(x=250,y=200)

        def func2():
            q1status,q2status=ts.display()

            if ts.is_empty("1") and (ts.is_empty("2")==False):
                messagebox.showinfo("CURRENT STATUS", "No work pending in service point 1"+"                  "+"Orders Pending in Service point 2"+str(q2status))

            elif ts.is_empty("2") and (ts.is_empty("1")==False):
                messagebox.showinfo("CURRENT STATUS","Orders Pending in Service point 1"+str(q1status)+"                  "+"No work pending in service point 2")
                
            elif ts.is_empty("1") and ts.is_empty("2"):
                messagebox.showinfo("CURRENT STATUS","No work pending in both service points")

            elif ts.is_empty("1")==False and ts.is_empty("2")==False:
                messagebox.showinfo("CURRENT STATUS","Orders Pending in Service point 1"+str(q1status)+"                  "+"Orders Pending in Service point 2"+str(q2status))

            
        label2=tk.Label(window,text="CLICK TO VIEW CURRENT STATUS",font=("Comic Sans MS", 10, "bold"))
        label2.place(x=150,y=260)

        #create a button to display the two queues
        button2=tk.Button(window, text="CURRENT STATUS",fg="red",bg="black",font=("gotham", 10, "bold"),command=func2)
        button2.place(x=200,y=300)

        window.mainloop()

