import tkinter as tk
from tkinter import ttk, messagebox
from dbconnections import get_connection   #  Import connection

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
                                 bd=4, relief="raised",command=self.search_student, bg="light grey",
                                 width=30, font=("Arial", 16, "bold"), height=2)
        Searchbutton.grid(row=2, column=0, padx=60, pady=40)

        Deletebutton = tk.Button(optFrame, command=self.delete_student, text="REMOVE STUDENT",
                                 bd=4, relief="raised", bg="light grey",
                                 width=30, font=("Arial", 16, "bold"), height=2)
        Deletebutton.grid(row=3, column=0, padx=60, pady=40)

        updbutton = tk.Button(optFrame, text="UPDATE STUDENT",
                              bd=4, relief="raised",command= self.updateFrameFun,bg="light grey",
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

        self.addWin = tk.Toplevel(self.root)
        self.addWin.title("ADD_STUDENT_DETAIL")
        self.addWin.geometry("500x600")
        self.addWin.config(bg=self.clr(200, 220, 250))


        # Entry fields
        tk.Label(self.addWin, text="Roll_no:", bg=self.clr(150,180,250),
                 font=("arial",15,"bold")).grid(row=0, column=0, padx=20, pady=30)
        self.rollNo = tk.Entry(self.addWin, width=20, font=("arial",15,"bold"), bd=3)
        self.rollNo.grid(row=0, column=1, padx=10, pady=30)

        tk.Label(self.addWin, text="Name:", bg=self.clr(150,180,250),
                 font=("arial",15,"bold")).grid(row=1, column=0, padx=20, pady=30)
        self.Name_of_stud = tk.Entry(self.addWin, width=20, font=("arial",15,"bold"), bd=3)
        self.Name_of_stud.grid(row=1, column=1, padx=10, pady=20)

        tk.Label(self.addWin, text="F_Name:", bg=self.clr(150,180,250),
                 font=("arial",15,"bold")).grid(row=2, column=0, padx=20, pady=30)
        self.fName_of_stud = tk.Entry(self.addWin, width=20, font=("arial",15,"bold"), bd=3)
        self.fName_of_stud.grid(row=2, column=1, padx=10, pady=20)

        tk.Label(self.addWin, text="Subject:", bg=self.clr(150,180,250),
                 font=("arial",15,"bold")).grid(row=3, column=0, padx=20, pady=30)
        self.Subject = tk.Entry(self.addWin, width=20, font=("arial",15,"bold"), bd=3)
        self.Subject.grid(row=3, column=1, padx=10, pady=20)

        tk.Label(self.addWin, text="Grades:", bg=self.clr(150,180,250),
                 font=("arial",15,"bold")).grid(row=4, column=0, padx=20, pady=30)
        self.Grades = tk.Entry(self.addWin, width=20, font=("arial",15,"bold"), bd=3)
        self.Grades.grid(row=4, column=1, padx=10, pady=20)

        Submitbutton1 = tk.Button(self.addWin, command=self.addfun, text="Submit_Info",
                                  bd=2, relief="raised", bg="light grey",
                                  width=20, font=("Arial",16,"bold"), height=1)
        Submitbutton1.grid(row=5, column=1, padx=10, pady=14) 


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
                cur.execute(
                    "INSERT INTO student (rollNo, name, fname, sub, grade) VALUES (%s,%s,%s,%s,%s)",
                    (int(rn), name, fname, sub, grade)
                )
                con.commit()
                self.show_all_students()
                con.close()

                messagebox.showinfo("Success", f"Student {name} with Roll_no {rn} is Registered!")
                self.addWin.destroy()  # <- fixed

            except Exception as e:
                messagebox.showerror("Error", f"Error: {e}")
                self.addWin.destroy()  # <- fixed
        else:
            messagebox.showerror("Error", "Please Fill all input fields")


    def show_all_students(self):
        try:
            con = get_connection()
            cur = con.cursor()  
            cur.execute("SELECT * FROM student ORDER BY rollNo ASC")
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
    
    def updateFrameFun(self):
        self.updateWin = tk.Toplevel(self.root)
        self.updateWin.title("UPDATE_STUDENT_DETAIL")
        self.updateWin.geometry("500x400")
        self.updateWin.config(bg=self.clr(200, 220, 250))
        self.updateWin.transient(self.root)
        self.updateWin.grab_set()
        self.updateWin.focus()

        # Roll number entry (to identify student)
        tk.Label(self.updateWin, text="Roll_no:", bg=self.clr(150,180,250),
                font=("arial",15,"bold")).grid(row=0, column=0, padx=20, pady=20)
        self.updateRollNo = tk.Entry(self.updateWin, width=20, font=("arial",15,"bold"), bd=3)
        self.updateRollNo.grid(row=0, column=1, padx=10, pady=20)

        # Dropdown to choose field to update
        tk.Label(self.updateWin, text="Field to Update:", bg=self.clr(150,180,250),
                font=("arial",15,"bold")).grid(row=1, column=0, padx=20, pady=20)
        self.updateField = ttk.Combobox(self.updateWin, values=["Name", "F_Name", "Both"], state="readonly",
                                        font=("arial", 14))
        self.updateField.bind("<<ComboboxSelected>>", self.on_field_change)
        self.updateField.grid(row=1, column=1, padx=10, pady=20)
        self.updateField.current(0)  # default to "Name"

        # Entry fields for new values
        self.updatenameLabel = tk.Label(self.updateWin, text="New Name:", bg=self.clr(150,180,250),
                               font=("arial",15,"bold"))
        self.updateName = tk.Entry(self.updateWin, width=20, font=("arial",15,"bold"), bd=3)

        self.updateFnameLabel = tk.Label(self.updateWin, text="New F_Name:", bg=self.clr(150,180,250),
                                 font=("arial",15,"bold"))
        self.updateFName = tk.Entry(self.updateWin, width=20, font=("arial",15,"bold"), bd=3)

        # Submit button
        tk.Button(self.updateWin, text="Update Info", command=self.updatefun,
                bd=2, relief="raised", bg="light grey",
                width=20, font=("Arial",16,"bold"), height=1).grid(row=4, column=1, pady=20)
        
    def on_field_change(self, event):
        field = self.updateField.get()

        # hide everything first
        self.updatenameLabel.grid_forget()
        self.updateName.grid_forget()
        self.updateFnameLabel.grid_forget()
        self.updateFName.grid_forget()

        # show based on selection
        if field == "Name":
            self.updatenameLabel.grid(row=2, column=0, padx=20, pady=10)
            self.updateName.grid(row=2, column=1, padx=10, pady=10)
        elif field == "F_Name":
            self.updateFnameLabel.grid(row=3, column=0, padx=20, pady=10)
            self.updateFName.grid(row=3, column=1, padx=10, pady=10)
        elif field == "Both":
            self.updatenameLabel.grid(row=2, column=0, padx=20, pady=10)
            self.updateName.grid(row=2, column=1, padx=10, pady=10)
            self.updateFnameLabel.grid(row=3, column=0, padx=20, pady=10)
            self.updateFName.grid(row=3, column=1, padx=10, pady=10)





    def updatefun(self):
        rn = self.updateRollNo.get()
        field = self.updateField.get()
        name = self.updateName.get()
        fname = self.updateFName.get()

        if not rn:
            messagebox.showerror("Error", "Please enter Roll Number")
            return

        try:
            rn_int = int(rn)
        except ValueError:
            messagebox.showerror("Error", "Roll Number must be numeric")
            return

        if field == "Name" and not name:
            messagebox.showerror("Error", "Enter New Name")
            return
        if field == "F_Name" and not fname:
            messagebox.showerror("Error", "Enter New F_Name")
            return
        if field == "Both" and not (name and fname):
            messagebox.showerror("Error", "Enter both Name and F_Name")
            return

        try:
            con = get_connection()
            cur = con.cursor()

            if field == "Name":
                cur.execute("UPDATE student SET name=%s WHERE rollNo=%s", (name, rn_int))
            elif field == "F_Name":
                cur.execute("UPDATE student SET fname=%s WHERE rollNo=%s", (fname, rn_int))
            else:  # Both
                cur.execute("UPDATE student SET name=%s, fname=%s WHERE rollNo=%s", (name, fname, rn_int))

            con.commit()
            self.show_all_students()
            con.close()

            messagebox.showinfo("Success", f"Student with Roll_no {rn_int} Updated!")
            self.updateWin.destroy()

        except Exception as e:
            messagebox.showerror("Error", f"Error: {e}")


    
    def search_student(self):
    # Create a small popup window for search
        search_win = tk.Toplevel(self.root)
        search_win.title("Search Student")
        search_win.geometry("400x200")
        search_win.config(bg=self.clr(200, 220, 250))

        # Roll No label + entry
        lbl = tk.Label(search_win, text="Enter Roll No:", font=("Arial", 14, "bold"), bg=self.clr(200, 220, 250))
        lbl.pack(pady=20)

        roll_entry = tk.Entry(search_win, font=("Arial", 14))
        roll_entry.pack(pady=10)

        def do_search():
            rn = roll_entry.get()
            if not rn.isdigit():
                messagebox.showerror("Error", "Please enter a valid Roll No (number)")
                return
            try:
                con = get_connection()
                cur = con.cursor()
                cur.execute("SELECT * FROM student WHERE rollNo=%s", (rn,))
                row = cur.fetchone()
                con.close()

                # Clear old table content
                self.table.delete(*self.table.get_children())

                if row:
                    self.table.insert('', tk.END, values=row)
                else:
                    messagebox.showinfo("Not Found", f"No student found with Roll No {rn}")

                search_win.destroy()
            except Exception as e:
                messagebox.showerror("Error", f"Error searching student: {e}")
                search_win.destroy()

        # Search button
        btn = tk.Button(search_win, text="Search", font=("Arial", 14, "bold"), bg="light grey", command=do_search)
        btn.pack(pady=10)




root = tk.Tk()
obj = std(root)
root.mainloop()

