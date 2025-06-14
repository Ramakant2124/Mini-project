from tkinter import *
from tkinter import messagebox

class Student:
    def __init__(self):
        self.sid = None
        self.name = ""
        self.age = 0
        self.marks = 0.0

    def add(self, i, n, a, m):
        self.sid = i
        self.name = n
        self.age = a
        self.marks = m

    def show(self):
        return f"ID: {self.sid}, Name: {self.name}, Age: {self.age}, Marks: {self.marks}"

# List to store student objects
l1 = []

# GUI Functions
def add_student():
    try:
        sid = int(entry_id.get())
        name = entry_name.get()
        age = int(entry_age.get())
        marks = float(entry_marks.get())
        s = Student()
        s.add(sid, name, age, marks)
        l1.append(s)
        messagebox.showinfo("Success", "Student Added Successfully")
        clear_entries()
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter correct values.")

def update_student():
    try:
        sid = int(entry_id.get())
        for s in l1:
            if s.sid == sid:
                s.name = entry_name.get()
                s.age = int(entry_age.get())
                s.marks = float(entry_marks.get())
                messagebox.showinfo("Success", "Student Updated Successfully")
                return
        messagebox.showwarning("Not Found", "Student ID not found.")
    except ValueError:
        messagebox.showerror("Error", "Invalid input.")

def delete_student():
    try:
        sid = int(entry_id.get())
        for s in l1:
            if s.sid == sid:
                l1.remove(s)
                messagebox.showinfo("Success", "Student Deleted Successfully")
                return
        messagebox.showwarning("Not Found", "Student ID not found.")
    except ValueError:
        messagebox.showerror("Error", "Invalid input.")

def show_students():
    text_area.delete(1.0, END)
    if not l1:
        text_area.insert(END, "No student records found.\n")
    else:
        for s in l1:
            text_area.insert(END, s.show() + "\n")

def clear_entries():
    entry_id.delete(0, END)
    entry_name.delete(0, END)
    entry_age.delete(0, END)
    entry_marks.delete(0, END)

# Tkinter GUI
root = Tk()
root.title("Student Management System")
root.configure(bg="cyan") 

# Labels and Entries
Label(root, font=('Arial', 10, 'bold'), text="Student ID", bg="cyan").grid(row=0, column=0, padx=10, pady=5)
entry_id = Entry(root)
entry_id.grid(row=0, column=1, padx=10, pady=5)

Label(root, font=('Arial', 10, 'bold'), text="Name", bg="cyan").grid(row=1, column=0, padx=10, pady=5)
entry_name = Entry(root)
entry_name.grid(row=1, column=1, padx=10, pady=5)

Label(root, font=('Arial', 10, 'bold'), text="Age", bg="cyan").grid(row=2, column=0, padx=10, pady=5)
entry_age = Entry(root)
entry_age.grid(row=2, column=1, padx=10, pady=5)

Label(root, font=('Arial', 10, 'bold'), text="Marks", bg="cyan").grid(row=3, column=0, padx=10, pady=5)
entry_marks = Entry(root)
entry_marks.grid(row=3, column=1, padx=10, pady=5)

# Buttons
Button(root, text="Add", width=12, command=add_student, bg="white").grid(row=4, column=0, pady=10)
Button(root, text="Update", width=12, command=update_student, bg="white").grid(row=4, column=1)
Button(root, text="Delete", width=12, command=delete_student, bg="white").grid(row=5, column=0, pady=5)
Button(root, text="Show All", width=12, command=show_students, bg="white").grid(row=5, column=1)

# Output Area
text_area = Text(root, width=50, height=10)
text_area.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
