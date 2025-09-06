import tkinter as tk
from tkinter import ttk, messagebox
from dbconnections import get_connection   # ✅ Import connection

class std:

    def __init__(self, root):
        self.root = root
        self.root.title("Student Record")

        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()
        self.root.geometry(f"{self.width}x{self.height}+0+0")

        title = tk.Label(self.root, text="Student Record Management System",
                         bd=4, relief="raised", bg=self.clr(140,180,100),
                         font=("Elephant", 40, "bold"))
        title.pack(side="top", fill="x")

        # Option Frame
        optFrame = tk.Frame(self.root, bd=5, relief="ridge", bg=self.clr(140,160,200))
        optFrame.place(width=self.width/3+20, height=self.height-202, x=50, y=100)

        addbutton = tk.Button(optFrame, command=self.addFrameFun, text="ADD STUDENT",
                              bd=4, relief="raised", bg="light grey",
                              width=30, font=("Arial", 16, "bold"), height=2)
        addbutton.grid(row=1, column=0, padx=60, pady=40)

        Searchbutton = tk.Button(optFrame, text="SEARCH STUDENT",
                                 bd=4, relief="raised", bg="light grey",
                                 width=30, font=("Arial", 16, "bold"), height=2)
        Searchbutton.grid(row=2, column=0, padx=60, pady=40)

        Deletebutton = tk.Button(optFrame, command=self.delete_student, text="REMOVE STUDENT",
                                 bd=4, relief="raised", bg="light grey",
                                 width=30, font=("Arial", 16, "bold"), height=2)
        Deletebutton.grid(row=3, column=0, padx=60, pady=40)

        updbutton = tk.Button(optFrame, text="UPDATE STUDENT",
                              bd=4, relief="raised", bg="light grey",
                              width=30, font=("Arial", 16, "bold"), height=2)
        updbutton.grid(row=4, column=0, padx=60, pady=40)

        showbutton = tk.Button(optFrame, command=self.show_all_students, text="SHOW ALL STUDENT",
                               bd=4, relief="raised", bg="light grey",
                               width=30, font=("Arial", 16, "bold"), height=2)
        showbutton.grid(row=5, column=0, padx=60, pady=40)

        # Detail Frame
        self.detFrame = tk.Frame(self.root, bd=5, relief="ridge", bg=self.clr(200,120,120))
        self.detFrame.place(width=self.width/2+40, height=self.height-203,
                            x=self.width/3+100, y=100)

        lbl = tk.Label(self.detFrame, text="STUDENT DETAILS",
                       font=("Arial", 30, "bold"), bg=self.clr(200,120,120))
        lbl.pack(side="top", fill="x")

        self.tab()


    def tab(self):
        tabframe = tk.Frame(self.detFrame, bd=4, relief="sunken", bg=self.clr(120,140,160))
        tabframe.place(width=self.width/2.1, height=self.height-300, x=35, y=70)

        x_scrol = tk.Scrollbar(tabframe, orient="horizontal")
        x_scrol.pack(side="bottom", fill="x")

        y_scrol = tk.Scrollbar(tabframe, orient="vertical")
        y_scrol.pack(side="right", fill="y")

        self.table = ttk.Treeview(tabframe,
                                  xscrollcommand=x_scrol.set,
                                  yscrollcommand=y_scrol.set,
                                  columns=("roll_no","name","fname","sub","grade"))

        x_scrol.config(command=self.table.xview)
        y_scrol.config(command=self.table.yview)

        self.table.heading("roll_no", text="ROLL_NO")
        self.table.heading("name", text="NAME")
        self.table.heading("fname", text="Father_Name")
        self.table.heading("sub", text="SUBJECT")
        self.table.heading("grade", text="GRADE")
        self.table["show"] = "headings"

        self.table.pack(fill="both", expand=1)

    def addFrameFun(self):
        if hasattr(self, 'addFrame') and self.addFrame.winfo_exists():
            self.addFrame.destroy()

        self.addFrame = tk.Frame(self.root, bd=5, relief="ridge", bg=self.clr(150,180,250))
        self.addFrame.place(width=self.width/3, height=self.height-330, x=self.width/3+80, y=100)

        # Entry fields
        tk.Label(self.addFrame, text="Roll_no:", bg=self.clr(150,180,250),
                 font=("arial",15,"bold")).grid(row=0, column=0, padx=20, pady=30)
        self.rollNo = tk.Entry(self.addFrame, width=20, font=("arial",15,"bold"), bd=3)
        self.rollNo.grid(row=0, column=1, padx=10, pady=30)

        tk.Label(self.addFrame, text="Name:", bg=self.clr(150,180,250),
                 font=("arial",15,"bold")).grid(row=1, column=0, padx=20, pady=30)
        self.Name_of_stud = tk.Entry(self.addFrame, width=20, font=("arial",15,"bold"), bd=3)
        self.Name_of_stud.grid(row=1, column=1, padx=10, pady=20)

        tk.Label(self.addFrame, text="F_Name:", bg=self.clr(150,180,250),
                 font=("arial",15,"bold")).grid(row=2, column=0, padx=20, pady=30)
        self.fName_of_stud = tk.Entry(self.addFrame, width=20, font=("arial",15,"bold"), bd=3)
        self.fName_of_stud.grid(row=2, column=1, padx=10, pady=20)

        tk.Label(self.addFrame, text="Subject:", bg=self.clr(150,180,250),
                 font=("arial",15,"bold")).grid(row=3, column=0, padx=20, pady=30)
        self.Subject = tk.Entry(self.addFrame, width=20, font=("arial",15,"bold"), bd=3)
        self.Subject.grid(row=3, column=1, padx=10, pady=20)

        tk.Label(self.addFrame, text="Grades:", bg=self.clr(150,180,250),
                 font=("arial",15,"bold")).grid(row=4, column=0, padx=20, pady=30)
        self.Grades = tk.Entry(self.addFrame, width=20, font=("arial",15,"bold"), bd=3)
        self.Grades.grid(row=4, column=1, padx=10, pady=20)

        Submitbutton1 = tk.Button(self.addFrame, command=self.addfun, text="Submit_Info",
                                  bd=2, relief="raised", bg="light grey",
                                  width=20, font=("Arial",16,"bold"), height=1)
        Submitbutton1.grid(row=5, column=1, padx=10, pady=14) 

        cancelbutton = tk.Button(self.addFrame, text="Cancel", bd=2, relief="raised",
                                 bg="light grey", width=20, font=("Arial",16,"bold"), height=1,
                                 command=self.addFrame.destroy)
        cancelbutton.grid(row=6, column=1, padx=10, pady=10)

    def addfun(self):
        rn = self.rollNo.get()
        name = self.Name_of_stud.get()
        fname = self.fName_of_stud.get()
        sub = self.Subject.get()
        grade = self.Grades.get()

        if rn and name and fname and sub and grade:
            try:
                con = get_connection()
                cur = con.cursor()
                cur.execute("INSERT INTO student (rollNo, name, fname, sub, grade) VALUES (%s,%s,%s,%s,%s)",
                            (int(rn), name, fname, sub, grade))
                con.commit()
                self.show_all_students()
                con.close()

                messagebox.showinfo("Success", f"Student {name} with Roll_no {rn} is Registered!")

                self.addFrame.destroy()

            except Exception as e:
                messagebox.showerror("Error", f"Error: {e}")
                self.addFrame.destroy()
        else:
            messagebox.showerror("Error", "Please Fill all input fields")

    def show_all_students(self):
        try:
            con = get_connection()
            cur = con.cursor()
            cur.execute("SELECT * FROM student")
            rows = cur.fetchall()
            con.close()

            # Clear old table content
            self.table.delete(*self.table.get_children())

            # Insert all rows into Treeview
            for row in rows:
                self.table.insert('', tk.END, values=row)

        except Exception as e:
            messagebox.showerror("Error", f"Error loading data: {e}")

    def delete_student(self):
        """Delete selected student from DB and refresh table"""
        selected_item = self.table.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select a student to delete")
            return

        roll_no = self.table.item(selected_item, "values")[0]  # Get rollNo from first column

        try:
            con = get_connection()
            cur = con.cursor()
            cur.execute("DELETE FROM student WHERE rollNo=%s", (roll_no,))
            con.commit()
            self.show_all_students()
            con.close()

            messagebox.showinfo("Success", f"Student with Roll_no {roll_no} deleted successfully!")


        except Exception as e:
            messagebox.showerror("Error", f"Error deleting data: {e}")

    def clr(self,r,g,b):
        return f"#{r:02x}{g:02x}{b:02x}"


root = tk.Tk()
obj = std(root)
root.mainloop()

