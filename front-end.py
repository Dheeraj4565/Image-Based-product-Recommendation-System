from tkinter import *
from tkinter import messagebox as ms
import tkinter as tk
import sqlite3

with sqlite3.connect('quit.db') as db:
    c = db.cursor()

c.execute('CREATE TABLE IF NOT EXISTS user (username TEXT NOT NULL ,password TEX NOT NULL);')
db.commit()
db.close()


class intro:

    def __init__(self, master):
        self.master = master
        self.master.title("INTRO PAGE")
        self.widgets()

    def introo(self):
        self.newWindow = Toplevel(self.master)
        self.app = main(self.newWindow)

    def widgets(self):
        self.root = root
        img = tk.PhotoImage(file="C:\\Users\\dheeraj\\recommendation-system\\images\\shop1.png")
        self.head = Label(self.master, text='WELCOME TO IMAGE BASED PRODUCT RECOMMENDATION', font=('Helvetica', 10, 'bold'), pady=10,
                          bg='black', fg='red')
        self.head.pack(expand=1, fill=tk.X)
        self.lbl = tk.Label(root, image=img, height=500, width=500, bg='red').pack()
        self.button1 = tk.Button(root, text="    CONTINUE  : ) ", font=('Times', 15, 'bold'), bd=6, bg='yellow',
                                 fg='black', command=self.introo)
        self.button1.place(x=160, y=400)

        self.root.mainloop()


class main():

    def __init__(self, master):
        self.master = master
        self.username = StringVar()
        self.password = StringVar()
        self.n_username = StringVar()
        self.n_password = StringVar()
        self.address = StringVar()
        self.phone = StringVar()
        self.email = StringVar()
        self.widgets()
        self.master.title("Login Page")

    def login(self):
        with sqlite3.connect('quit.db') as db:
            c = db.cursor()

        find_user = ('SELECT * FROM user WHERE username = ? and password = ?')
        c.execute(find_user, [(self.username.get()), (self.password.get())])
        result = c.fetchall()
        if result:
            self.logf.pack_forget()
            ms.showinfo('logged in succesfully', self.username.get() + '\n Logged In')
            self.head['pady'] = 150
            self.newWindow = Toplevel(self.master)
            self.app = eshopi(self.newWindow)
        else:
            ms.showerror('Oops!', 'Username Not Found.')

    def new_user(self):
        with sqlite3.connect('quit.db') as db:
            c = db.cursor()
        find_user = ('SELECT * FROM user WHERE username = ?')
        c.execute(find_user, [(self.username.get())])
        if c.fetchall():
            ms.showerror('Error!', 'Username Taken Try a Diffrent One.')
        else:
            ms.showinfo('Success!', 'Account Created! , Click On CONTINUE TO SHOP! and Login')
            self.log()
            insert = 'INSERT INTO user(username,password) VALUES(?,?)'
            c.execute(insert, [(self.n_username.get()), (self.n_password.get())])
            db.commit()

    def update(self):
        u = self.username.get()
        p = self.password.get()

        if (self.username.get() == "" or self.password.get() == ""):
            ms.askokcancel("Reset Password", "please fill all details!!!")
        else:
            conn = sqlite3.connect('quit.db')
            with conn:
                cursor = conn.cursor
                conn.execute("UPDATE user SET password=? WHERE username=?", (p, u))
                ms.askokcancel("Reset Password", "Password is updated!!!,Click on Continue To Shop")
                conn.commit()

    def log(self):
        self.username.set('')
        self.password.set('')
        self.crf.pack_forget()
        self.head['text'] = 'Login User'
        self.logf.pack()

    def cr(self):
        self.n_username.set('')
        self.n_password.set('')
        self.address.set('')
        self.phone.set('')
        self.email.set('')
        self.logf.pack_forget()
        self.head['text'] = 'Create Account'
        self.crf.pack()

    def up(self):
        self.username.set('')
        self.password.set('')
        self.crf.pack_forget()
        self.logf.pack_forget()
        self.head['text'] = 'Forgot Password ?'
        self.upf.pack()

    def widgets(self):
        self.head = Label(self.master, text='LOGIN USER', bg='black', fg='red', font=('', 35), pady=10)
        self.head.pack(expand=1, fill=tk.X)
        self.logf = Frame(self.master, bg='red', padx=10, pady=10)
        Label(self.logf, text='Username: ', font=('', 20), bg='red', pady=5, padx=5).grid(sticky=W)
        Entry(self.logf, textvariable=self.username, bd=5, font=('', 15)).grid(row=0, column=1)
        Label(self.logf, text='Password: ', font=('', 20), bg='red', pady=5, padx=5).grid(sticky=W)
        Entry(self.logf, textvariable=self.password, bd=5, font=('', 15), show='*').grid(row=1, column=1)
        Button(self.logf, text=' Login ', bd=5, font=('', 15), width=16, bg='blue', fg='white', padx=5, pady=5,
               command=self.login).grid()
        Button(self.logf, text=' Create Account ', bd=5, font=('', 15), width=16, bg='blue', fg='white', padx=5, pady=5,
               command=self.cr).grid(row=2, column=1)
        Button(self.logf, text=' forgot password ? ', bd=5, font=('', 15), width=16, bg='blue', fg='white', padx=5,
               pady=5, command=self.up).grid(row=2, column=2)
        self.logf.pack(expand=1, fill=tk.X)

        self.crf = Frame(self.master, bg='blue', padx=10, pady=10)
        Label(self.crf, text='Username: ', font=('', 20), bg='blue', fg='white', pady=5, padx=5).grid(sticky=W)
        Entry(self.crf, textvariable=self.n_username, bd=5, font=('', 15)).grid(row=0, column=1)
        Label(self.crf, text='Password: ', font=('', 20), bg='blue', fg='white', pady=5, padx=5).grid(sticky=W)
        Entry(self.crf, textvariable=self.n_password, bd=5, font=('', 15), show='*').grid(row=1, column=1)
        Label(self.crf, text='Address: ', font=('', 20), bg='blue', fg='white', pady=5, padx=5).grid(sticky=W)
        Entry(self.crf, textvariable=self.address, bd=5, font=('', 15)).grid(row=2, column=1)
        Label(self.crf, text='Phone no.: ', font=('', 20), bg='blue', fg='white', pady=5, padx=5).grid(sticky=W)
        Entry(self.crf, textvariable=self.phone, bd=5, font=('', 15)).grid(row=3, column=1)
        Label(self.crf, text='email: ', font=('', 20), bg='blue', fg='white', pady=5, padx=5).grid(sticky=W)
        Entry(self.crf, textvariable=self.email, bd=5, font=('', 15)).grid(row=4, column=1)
        Button(self.crf, text='Create Account', bd=5, font=('', 15), width=16, bg='yellow', padx=5, pady=5,
               command=self.new_user).grid()
        Button(self.crf, text='Go to Login', bd=5, font=('', 15), width=16, bg='yellow', padx=5, pady=5,
               command=self.log).grid(row=5, column=1)

        self.upf = Frame(self.master, bg='yellow', padx=10, pady=10)
        Label(self.upf, text='Username: ', font=('', 20), bg='yellow', pady=5, padx=5).grid(sticky=W)
        Entry(self.upf, textvariable=self.username, bd=5, font=('', 15)).grid(row=0, column=1)
        Label(self.upf, text='New Password: ', font=('', 20), bg='yellow', pady=5, padx=5).grid(sticky=W)
        Entry(self.upf, textvariable=self.password, bd=5, font=('', 15), show='*').grid(row=1, column=1)
        Button(self.upf, text=' Update Your Password', bd=5, font=('', 15), width=18, bg='blue', fg='white', padx=5,
               pady=5, command=self.update).grid(row=4, column=1)

        #def showimage():
            #fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Select Image File",filetypes=(("JPG file","*.JPG"),("PNG file","*.PNG"),("JPG file","*.JPG"),("All Files","*.*")))


class eshopi:
    def __init__(self, master):
        self.master = master
        self.master.title("Recommendation System")
        self.master.geometry("1000x800")
        self.widgets2()

    def helloCallBack(self):
        exec(open("Back-end.py").read())



    def widgets2(self):
        self.newframe = Frame(self.master, height=800, width=9000)
        self.c = Canvas(self.master, bg="deep sky blue", height=700, width=1200)
        self.c.pack(expand=YES, fill=BOTH)
        self.img = tk.PhotoImage(file="C:\\Users\\dheeraj\\recommendation-system\\images\\firstmain.png")
        self.lbl = tk.Label(self.c, image=self.img, height=800, width=9000).pack()
        self.b = Button(self.c, text="Upload Image", bd=10, width=15, font=('', 15), bg='red', fg='white', padx=5, pady=5,
                        command=self.helloCallBack)
        self.b.place(x=400, y=450)

        self.c.pack()



root = Tk()
intro(root)
root.mainloop()
