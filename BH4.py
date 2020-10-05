from tkinter import *
import sqlite3

root = Tk()
root.title("Dustbin 2.0")
conn = sqlite3.connect("BB4.db")
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS bb4(id integer primary key autoincrement , username TEXT, password TEXT,credits integer ,sqltime TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL)")
conn.commit()
conn.close()

def click():
    t = Toplevel()
    t.title("Your account")
    conn = sqlite3.connect("BB4.db")
    c = conn.cursor()
    c.execute("UPDATE bb4 SET credits = credits + 50 WHERE password=?;", (e2.get(),))
    conn.commit()
    r = c.fetchall()
    print(r)
    # l=Label(t, text="Your current credits are: "+r).pack()
    conn.close()
    print("saved")

    l = Label(t, text="50 credits added to your account " + e1.get()).pack()




def open():
    top = Toplevel()
    top.title("Type of waste")
    lb = Label(top, text="Enter type of waste").pack()
    b1 = Button(top, text="Wet", command=click).pack()
    b2 = Button(top, text="Dry", command=click).pack()
    b3 = Button(top, text="Plastic", command=click).pack()


def save():
    tt= Toplevel()
    b = Button(tt, text="Continue", command=open)
    conn = sqlite3.connect('BB4.db')
    c = conn.cursor()
    c.execute('INSERT INTO bb4(username,password,credits) VALUES (?,?,?)', (e11.get(), e22.get(), 50))
    conn.commit()
    b.place(x=50,y=50,width=125,height=30)
    print("Saved Data")




myLabel1 = Label(root, text="Dustbin 2.0")
name = Label(root, text="Username")
pas = Label(root, text="Password")
e1 = Entry(root, width=50)
e2 = Entry(root, width=50)
b = Button(root, text="Login", command=open)
myLabel1.grid(row=0, column=2)
name.grid(row=1, column=0)
pas.grid(row=2, column=0)
b.grid(row=3, column=2)
e1.grid(row=1, column=2)
e2.grid(row=2, column=2)
ll=Label(root, text="New User? Register Below")
ll.grid(row=4, column=2)
l1 = Label(root, text="Username")
l2 = Label(root, text="Password")
b0 = Button(root, text="Save", command=save)
e11 = Entry(root, width=50)
e22 = Entry(root, width=50)
l1.grid(row=5, column=0)
l2.grid(row=6, column=0)
e11.grid(row=5, column=2)
e22.grid(row=6, column=2)
b0.grid(row=7, column=2)

root.mainloop()