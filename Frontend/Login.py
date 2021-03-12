
from tkinter import *
from tkinter import messagebox

from PIL import ImageTk

import Backend.dbconnection
import Frontend.MayaAi
from Frontend import Register


class login_page:
    def __init__(self, root):
        """ This is the Login Page for registration for Assistant Maya where it has login interface"""
        self.root = root
        self.root.title('Login')
        self.root.geometry("555x735+400+0")
        self.root.resizable(0, 0)

        self.db = Backend.dbconnection.Dbconnect()

        self.bg = ImageTk.PhotoImage(file="C:/Users/Hp/RsDev/Project1/Frontend/Background.jpg")
        Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        self.left = ImageTk.PhotoImage(file="C:/Users/Hp/RsDev/Project1/Frontend/Logo.jpg")
        Label(self.root, image=self.left).place(x=30, y=40, width=500, height=250)

        frame1 = Frame(self.root, bg="orange")
        frame1.place(x=30, y=290, width=498, height=400)

        Label(frame1, text="Login Here", font=("times new roman", 25, "bold"),
                      bg="orange", fg="green").place(x=30, y=30)

        Email = Label(frame1, text="Email Address", font=("times new roman", 17),
                      bg="orange", fg="black").place(x=100, y=90)
        self.text_email = Entry(frame1, font=("times new roman", 16), bg="orange")
        self.text_email.place(x=100, y=130, width=300)

        passwords = Label(frame1, text="Password", font=("times new roman", 17), bg="orange",
                         fg="black").place(x=100, y=170)
        self.text_password = Entry(frame1, font=("times new roman", 16), bg="orange",show="*")
        self.text_password.place(x=100, y=210, width=300)

        btn_login = Button(self.root, text="Log In", command=self.login_data, font=("times new roman", 15),
                           bd=0, cursor="hand2").place(x=180, y=560, width=200, height=40)

        btn_register = Button(self.root, text="Register", command=self.register_window, font=("times new roman", 14),
                              bd=0, cursor="hand2").place(x=180, y=670, width=200, height=40)

    def register_window(self):
        tk = Toplevel()
        Register.Register(tk)
        self.root.withdraw()

    def login_data(self):
        """ Here it has functions for email and password for entering into
        Main Run Maya GUI Interface where it requires verification"""
        Email = self.text_email.get()
        passwords = self.text_password.get()

        if self.text_email.get() == "" or self.text_password.get() == "":
            messagebox.showerror("Error", "please fill the empty field", parent=self.root)

        else:
            query = "select * from rohit_tbl_users where Email_ID=%s and Password_=%s"
            values = (Email, passwords)
            rows = self.db.select(query, values)
            data = []
            print(rows)
            if len(rows) != 0:
                for row in rows:
                    data.append(row[3])
                    data.append(row[6])
                print(data)
                if Email == data[0] and passwords == data[1]:

                    messagebox.showinfo('Success', 'Congratulations!! login successfully',parent=self.root)
                    self.root.destroy()
                    Frontend.MayaAi.wishMe()
                    Frontend.MayaAi.Widget()


                else:
                    messagebox.showerror('Error', 'Invalid email and password', parent=self.root)
            else:
                messagebox.showinfo("Error", "User not registered !! Register first", parent=self.root)

#
# root = Tk()
# obj = login_page(root)
# root.mainloop()