import tkinter as tk
from tkinter import ttk
class std():
    def __init__(self,root):
        self.root=root
        self.root.title("student Record")
        
        self.width=self.root.winfo_screenwidth()
        self.height= self.root.winfo_screenheight()
        self.root.geometry(f"{self.width}x{self.height}+0+0")

        title=tk.Label(self.root,text="Student record Management System",bd=4,relief="raised",bg=self.clr(100,180,100),font=("Elephant",40,"bold"))

        title.pack(side="top",fill="x")

        #option frame
        optFrame=tk.Frame(self.root,bd=5,relief="ridge",bg=self.clr(140,160,200))
        optFrame.place(width=self.width/3+20,height=self.height-202,x=50,y=100)

        addbutton=tk.Button(optFrame,text="ADD STUDENT",bd=4,relief="raised",bg="light grey",width=30,font=("Arial",16,"bold"),height=2)

        addbutton.grid(row=1,column=0,padx=60,pady=40) 

        Searchbutton=tk.Button(optFrame,text="SEARCH STUDENT",bd=4,relief="raised",bg="light grey",width=30,font=("Arial",16,"bold"),height=2)

        Searchbutton.grid(row=2,column=0,padx=60,pady=40) 

        Deletebutton=tk.Button(optFrame,text="REMOVE STUDENT",bd=4,relief="raised",bg="light grey",width=30,font=("Arial",16,"bold"),height=2)

        Deletebutton.grid(row=3,column=0,padx=60,pady=40) 

        updbutton=tk.Button(optFrame,text="UPDATE STUDENT",bd=4,relief="raised",bg="light grey",width=30,font=("Arial",16,"bold"),height=2)

        updbutton.grid(row=4,column=0,padx=60,pady=40) 

        showbutton=tk.Button(optFrame,text="SHOW ALL STUDENT",bd=4,relief="raised",bg="light grey",width=30,font=("Arial",16,"bold"),height=2)

        showbutton.grid(row=5,column=0,padx=60,pady=40) 

        #detail frame
        self.detFrame=tk.Frame(self.root,bd=5,relief="ridge",bg=self.clr(200,120,120))
        self.detFrame.place(width=self.width/2+40,height=self.height-203,x=self.width/3+100,y=100)


        lbl=tk.Label(self.detFrame,text="STUDENT DETAILS",font=("Arial",30,"bold"),bg=self.clr(200,120,120))

        lbl.pack(side="top",fill="x")

        self.tab()
    
    def tab(self):
        tabframe=tk.Frame(self.detFrame,bd=4,relief="sunken",bg=self.clr(120,140,160))

        tabframe.place(width=self.width/2.1,height=self.height-300,x=35,y=70)

        x_scrol=tk.Scrollbar(tabframe,orient="horizontal")
        x_scrol.pack(side="bottom",fill="x")

        y_scrol=tk.Scrollbar(tabframe,orient="vertical")
        y_scrol.pack(side="right",fill="y")

        self.table=ttk.Treeview(tabframe,xscrollcommand=x_scrol.set,yscrollcommand=y_scrol.set,columns=("roll_no","name","fname","sub","grade"))

        x_scrol.config(command=self.table.xview)
        y_scrol.config(command=self.table.yview)
        self.table.heading("roll_no",text="ROLL_NO")
        self.table.heading("name",text="NAME")
        self.table.heading("fname",text="Father_Name")
        self.table.heading("sub",text="SUBJECT")
        self.table.heading("grade",text="GRADE")
        self.table["show"]="headings"

        self.table.pack(fill="both",expand=1)



    def clr(self,r,g,b):
        return f"#{r:02x}{g:02x}{b:02x}"


root= tk.Tk()
obj=std(root)
root.mainloop()