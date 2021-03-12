
from tkinter import *
from PIL import ImageTk
from tkinter import ttk
from tkinter import ttk, messagebox
import Model.User
import Backend.dbconnection
from Frontend.Login import login_page
from Frontend.View import View


class Register:
    def __init__(self, root):
        self.root = root
        self.root.title('Registration')
        self.root.geometry("555x735+400+0")
        self.root.resizable(0, 0)

        self.db = Backend.dbconnection.Dbconnect()

        self.bg = ImageTk.PhotoImage(file="C:/Users/Hp/RsDev/Project1/Frontend/Background.jpg")
        bg = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        self.left = ImageTk.PhotoImage(file="C:/Users/Hp/RsDev/Project1/Frontend/Logo.jpg")
        left = Label(self.root, image=self.left).place(x=30, y=10, width=500, height=150)

        frame1 = Frame(self.root, bg="orange")
        frame1.place(x=30, y=160, width=498, height=520)

        title = Label(frame1, text="Register Here", font=("times new roman", 20),
                      bg="orange", fg="red").place(x=30, y=30)

        Firstname = Label(frame1, text="First Name", font=("times new roman", 12),
                          bg="orange", fg="black").place(x=30, y=70)
        self.text_fname = Entry(frame1, font=("times new roman", 12), bg="orange")
        self.text_fname.place(x=30, y=100, width=200)
        #
        Lastname = Label(frame1, text="Last Name", font=("times new roman", 12),
                         bg="orange", fg="black").place(x=275, y=70)
        self.text_lname = Entry(frame1, font=("times new roman", 12), bg="orange")
        self.text_lname.place(x=275, y=100, width=200)
        #
        contact_No = Label(frame1, text="Contact Number", font=("times new roman", 12),
                           bg="orange", fg="black").place(x=30, y=130)
        self.text_contact = Entry(frame1, font=("times new roman", 12), bg="orange")
        self.text_contact.place(x=30, y=160, width=200)
        #
        Email_id = Label(frame1, text="Email", font=("times new roman", 12), bg="orange", fg="black") \
            .place(x=275, y=130)
        self.text_email = Entry(frame1, font=("times new roman", 12), bg="orange")
        self.text_email.place(x=275, y=160, width=200)

        #
        Security_question = Label(frame1, text="Security Question", font=("times new roman", 12),
                                  bg="orange", fg="black").place(x=30, y=190)
        self.cmb_quest = ttk.Combobox(frame1, font=("times new roman", 12), state="readonly")
        self.cmb_quest['values'] = ("Select", "Your Pet Name", "Your Birth Place", "Your Best friend Name")
        self.cmb_quest.place(x=30, y=220, width=200)
        self.cmb_quest.current(0)
        #
        Answer = Label(frame1, text="Answer", font=("times new roman", 12),
                       bg="orange", fg="black").place(x=275, y=190)
        self.text_Answer = Entry(frame1, font=("times new roman", 12), bg="orange")
        self.text_Answer.place(x=275, y=220, width=200)
        #
        passwords = Label(frame1, text="Password", font=("times new roman", 12), bg="orange",
                          fg="black").place(x=30, y=250)
        self.text_passwords = Entry(frame1, font=("times new roman", 12), bg="orange", show="*")
        self.text_passwords.place(x=30, y=280, width=200)

        conform_password = Label(frame1, text="Confirm Password", font=("times new roman", 12),
                                 bg="orange", fg="black").place(x=275, y=250)
        self.text_confpassword = Entry(frame1, font=("times new roman", 12), bg="orange", show="*")
        self.text_confpassword.place(x=275, y=280, width=200)
        #
        self.var_chkbox = IntVar()
        chkbox = Checkbutton(frame1, text=" I Agree The Terms & Conditions", variable=self.var_chkbox, cursor="hand2",
                             onvalue=1, offvalue=0, font=("times new roman", 10), bg="orange").place(x=30, y=310)

        btn_register = Button(frame1, text="Register", font=("times new roman", 14), bd=0, cursor="hand2",
                              command=self.Register_data).place(x=180, y=350, width=150, height=40)

        btn_login = Button(self.root, text="Sign In", command=self.login_window, font=("times new roman", 14),
                           bd=0, cursor="hand2").place(x=210, y=560, width=150, height=40)

        btn_View = Button(frame1, text="View",command=self.click_view, font=("times new roman", 14), bd=0, cursor="hand2", ) \
            .place(x=155, y=450, width=200, height=40)



    def login_window(self):
        tk = Toplevel()
        login_page(tk)
        self.root.withdraw()

    def click_view(self):
        # import Frontend.View
        tk = Toplevel()
        View(tk)
        # self.root.withdraw()



    def reset_clear(self):
        """ This reset_clear function works for clearing the frame after registration"""
        self.text_fname.delete(0, END),
        self.text_lname.delete(0, END),
        self.text_contact.delete(0, END),
        self.text_email.delete(0, END),
        self.cmb_quest.delete(0, END),
        self.text_Answer.delete(0, END),
        self.text_passwords.delete(0, END),
        self.text_confpassword.delete(0, END),
        self.cmb_quest.current(0)


    def Register_data(self):
        """ Here is the main registration system for verification
        where users have to input data for opening with verified for further operations   """
        First_name = self.text_fname.get()
        Last_name = self.text_lname.get()
        ContactNo = self.text_contact.get()
        Email_Id = self.text_email.get()
        Security_question = self.cmb_quest.get()
        Answer = self.text_Answer.get()
        Password_ = self.text_passwords.get()
        Confirm_password = self.text_confpassword.get()



        if self.text_fname.get() == "" or self.text_lname.get() == "" or self.text_contact.get() == "" \
                or self.text_email.get() == "" or self.cmb_quest.get() == "Select" or self.text_Answer.get() == "" \
                or self.text_passwords.get() == "" or self.text_confpassword.get() == "":
            messagebox.showerror("Error", "All fields should be fetched with data  ", parent=self.root)

        elif self.text_passwords.get() != self.text_confpassword.get():
            messagebox.showerror("Error", "Password doesn't match", parent=self.root)

        elif self.var_chkbox.get() == 0:
            messagebox.showerror("Error", "Our terms & Conditions Checkbox is Unchecked, Plz Mark It", parent=self.root)

        # ----Exception Handling---- #

        try:
            u = Model.User.User(First_name, Last_name, ContactNo, Email_Id, Security_question, Answer,
                                Password_, Confirm_password)

            query = "insert into rohit_tbl_users(First_name,Last_name,contact,Email_Id,Security_question,\
            Answer,Password_,Confirm_password) values(%s,%s,%s,%s,%s,%s,%s,%s)"

            values = (u.get_First_name(),
                      u.get_Last_name(),
                      u.get_contact(),
                      u.get_Email_Id(),
                      u.get_Security_question(),
                      u.get_Answer(),
                      u.get_Passwords(),
                      u.get_Confirm_password())


            self.db.insert(query, values)
            messagebox.showinfo("Success", "Register Successful", parent=self.root)
            from Frontend import Login
            self.reset_clear()

        except Exception as es:
            messagebox.showerror("Error",f"Error occurred due to {str(es)}", parent=self.root)

#
# root = Tk()
# obj = Register(root)
# root.mainloop()
