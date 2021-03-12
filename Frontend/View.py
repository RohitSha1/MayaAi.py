from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import Backend.dbconnection
import Model.User


# noinspection PyShadowingNames
class View:
    def __init__(self, root):
        self.root = root
        self.root.title("View Database of AImaya")
        self.root.geometry("1200x700+100+0")
        self.root.resizable(0, 0)

        self.db = Backend.dbconnection.Dbconnect()

        title = Label(self.root, text="DATABASE USER INTERFACE", bd=10, relief=GROOVE,
                      font=("times new roman", 30, "bold"), bg="white", fg="gold")
        title.pack(side=TOP, fill=X)


        #----Manage frame----#
        frame1 = Frame(self.root, bd=4, relief=RIDGE, bg="orange")
        frame1.place(x=0, y=100, width=260, height=580)

        m_title = Label(frame1, text="Manage Users", bg="orange", fg="White",
                        font=("times new roman", 15, "bold"))
        m_title.grid(row=0, columnspan=2, pady=20)

        #-----FirstName-----#

        Firstname = Label(frame1, text="First_name", bg="orange", fg="white", font=("times new roman", 15))
        Firstname.grid(row=1, sticky="w")
        self.text_fname = Entry(frame1, font=("times new roman", 12, "bold"), bd=2,
                              relief=GROOVE)
        self.text_fname.grid(row=2, sticky="w")

        #-------LastName------#

        Lastname = Label(frame1, text="Last_name", bg="orange", fg="white", font=("times new roman", 15))
        Lastname.grid(row=3, sticky="w")

        self.text_lname = Entry(frame1, font=("times new roman", 12, "bold"), bd=2,
                              relief=GROOVE)
        self.text_lname.grid(row=4,sticky="w")

        #-----Contact------#
        contact_No = Label(frame1, text="Contact", bg="orange", fg="white", font=("times new roman", 15))
        contact_No.grid(row=5, sticky="w")

        self.text_contact = Entry(frame1, font=("times new roman", 12, "bold"),bd=2,
                                 relief=GROOVE)
        self.text_contact.grid(row=6, sticky="w")

        #-------Email-------#
        Email_id = Label(frame1, text="Email", bg="orange", fg="white", font=("times new roman", 15))
        Email_id.grid(row=7, sticky="w")

        self.text_email = Entry(frame1, font=("times new roman", 12, "bold"), bd=2,
                                   relief=GROOVE)
        self.text_email.grid(row=8, sticky="w")


        #-----Security-question-----#
        Security_question = Label(frame1, text="Security Question", font=("times new roman", 12),
                                  bg="orange", fg="white").grid(row=9,sticky="w")
        self.cmb_quest = ttk.Combobox(frame1, font=("times new roman", 11), state="readonly")
        self.cmb_quest['values'] = ("Select", "Your Pet Name", "Your Birth Place", "Your Best friend Name")
        self.cmb_quest.grid(row=10,sticky="w")
        self.cmb_quest.current(0)

        #-----Answer-------#
        Answer = Label(frame1, text="Answer", font=("times new roman", 12),
                       bg="orange", fg="white").grid(row=11,sticky="w")
        self.text_Answer = Entry(frame1, font=("times new roman", 12), bg="white")
        self.text_Answer.grid(row=12,sticky="w")

        #------Password-------#
        passwords = Label(frame1, text="Password", bg="orange", fg="white", font=("times new roman", 15))
        passwords.grid(row=13, sticky="w")

        self.text_passwords = Entry(frame1, font=("times new roman", 12, "bold"), bd=2,
                             relief=GROOVE)
        self.text_passwords.grid(row=14,sticky="w")

        #-------ConformPassword---------#
        conform_password = Label(frame1, text="Confirm Password", bg="orange", fg="white", font=("times new roman", 15))
        conform_password.grid(row=15, sticky="w")

        self.text_confpassword = Entry(frame1, font=("times new roman", 12, "bold"), bd=2,
                                   relief=GROOVE)
        self.text_confpassword.grid(row=16, sticky="w")


        #-----button frame-----#
        btn_frame = Frame(frame1, bd=4, relief=RIDGE, bg="orange")
        btn_frame.place(x=10, y=500, width=420)

        #-------UpdateButton--------#
        Updatebtn = Button(btn_frame, text="Update",command=self.data_update, width=10).\
            grid(row=0, column=1, padx=10, pady=10)

        #--------DeleteButton-------#
        Deletebtn = Button(btn_frame, text="Delete",command=self.delete_data, width=10,).\
            grid(row=0, column=2, padx=10, pady=10)

        # -----Detail frame-------#
        detail_frame = Frame(self.root, bd=4, relief=RIDGE, bg="orange")
        detail_frame.place(x=299, y=100, width=850, height=580)

        #-------combobox-------#
        self.lbl_sort = Label(detail_frame, text="Sort By", bg="orange", fg="white", font=("times new roman", 20, "bold"))
        self.lbl_sort.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        self.combo_sort = ttk.Combobox(detail_frame, font=("poopins", 10, "bold"), state='readonly')
        self.combo_sort['values'] = ("Ascending", "Descending")
        self.combo_sort.current(0)
        self.combo_sort.grid(row=0, column=1, padx=20, pady=10)
        self.combo_sort.bind('<<ComboboxSelected>>', self.sorting)




        #-------SearchButton---------#
        self.text_search=StringVar()
        self.text_search = Entry(detail_frame, width=17,textvariable=self.text_search, font=("times new roman", 12), relief=GROOVE)
        self.text_search.grid(row=0, column=2, pady=10, padx=20, sticky="w")
        Searchbtn = Button(detail_frame, text="Search", command=self.search_data, width=10,
                           pady=5).grid(row=0, column=3, padx=10, pady=10)

        #---ShowButton-----#
        show_btn = Button(detail_frame, text="Show All",command=self.fetch_data, width=10, pady=5).grid(row=0, column=4, padx=10, pady=10)


        #-----Table frame-----#

        table_frame = Frame(detail_frame, bd=4, relief=RIDGE, bg="white")
        table_frame.place(x=0, y=70, width=820, height=500)

        scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)
        self.User_tbl = ttk.Treeview(table_frame,
                                     columns=("First_name", "Last_name", "contact","Email_Id","Security_question", "Answer", "Password"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.User_tbl.xview)
        scroll_y.config(command=self.User_tbl.yview)
        self.User_tbl.heading("First_name", text="First_Name")
        self.User_tbl.heading("Last_name", text="Last_Name")
        self.User_tbl.heading("contact", text="Contact")
        self.User_tbl.heading("Email_Id", text="Email")
        self.User_tbl.heading("Security_question", text="Security_question")
        self.User_tbl.heading("Answer", text="Answer",)
        self.User_tbl.heading("Password", text="Password",)
        self.User_tbl['show'] = 'headings'

        self.User_tbl.column("First_name", width=100)
        self.User_tbl.column("Last_name", width=100)
        self.User_tbl.column("contact", width=100)
        self.User_tbl.column("Email_Id", width=150)
        self.User_tbl.column("Security_question", width=130)
        self.User_tbl.column("Answer", width=100)
        self.User_tbl.column("Password", width=100)
        self.User_tbl.pack(fill=BOTH, expand=1)

        #------ Event Handling -----#
        self.User_tbl.bind("<ButtonRelease-1>",self.Reappear)
        self.clear_data()
        self.fetch_data()

    def fetch_data(self):
        """ this fetch_data function for fetching into GUI User Interface & in Database"""
        self.db = Backend.dbconnection.Dbconnect()
        query = 'select * from rohit_tbl_users'
        rows = self.db.selectall(query)
        if len(rows) != 0:
            self.User_tbl.delete(*self.User_tbl.get_children())
            for rows in rows:
                self.User_tbl.insert('', END, values=rows)

    def clear_data(self):
        self.text_fname.delete(0, END)
        self.text_lname.delete(0, END)
        self.text_contact.delete(0, END)
        self.text_email.delete(0, END)
        self.cmb_quest.delete(0, END),
        self.text_Answer.delete(0, END),
        self.text_passwords.delete(0, END)
        self.text_confpassword.delete(0, END)

        self.text_fname.insert(0, "")
        self.text_lname.insert(0, "")
        self.text_contact.insert(0, "")
        self.text_email.insert(0, "")
        self.cmb_quest.insert(0, "")
        self.text_Answer.insert(0, "")
        self.text_passwords.insert(0, "")
        self.text_confpassword.insert(0, "")

    def Reappear(self, event):
        """ Here Reappear function works for data reappearing into database and GUI fro showcasing"""
        cursor_rows = self.User_tbl.focus()
        contents =self.User_tbl.item(cursor_rows)
        row = contents['values']

        self.text_fname.delete(0, END)
        self.text_lname.delete(0, END)
        self.text_contact.delete(0, END)
        self.text_email.delete(0, END)
        self.text_passwords.delete(0, END),
        self.text_confpassword.delete(0, END)

        self.text_fname.insert(0,row[1])
        self.text_lname.insert(0,row[2])
        self.text_contact.insert(0,row[3])
        self.text_email.insert(0,row[4])
        self.cmb_quest.insert(0, row[5])
        self.text_Answer.insert(0, row[6])
        self.text_passwords.insert(0,row[7])
        # self.text_confpassword.insert(0,row[8])

    def data_update(self):
        """ This function will update data into database """
        First_name = self.text_fname.get()
        Last_name = self.text_lname.get()
        contact = self.text_contact.get()
        Email_Id = self.text_email.get()
        Security_question = self.cmb_quest.get()
        Answer = self.text_Answer.get()
        Password_ = self.text_passwords.get()
        Confirm_password = self.text_confpassword.get()

        u = Model.User.User(Email_Id, First_name, Last_name, contact, Security_question, Answer, Password_, Confirm_password )

        query = "update rohit_tbl_users set First_name=%s,Last_name=%s,contact=%s, Security_question=%s,Answer=%s,Password_=%s,Confirm_password=%s where Email_Id = %s"

        values = ( First_name, Last_name, contact, Security_question, Answer, Password_, Confirm_password,Email_Id)

        self.db.update(query, values)

        messagebox.showinfo('Success', 'data updated successfully')

        self.fetch_data()
        self.clear_data()

    def delete_data(self):
        """ Delete data is works in Users GUI for deletion the previous stored data"""
        First_name = self.text_fname.get()
        Last_name = self.text_lname.get()
        ContactNo = self.text_contact.get()
        Email_Id = self.text_email.get()
        Security_question = self.cmb_quest.get()
        Answer = self.text_Answer.get()
        Password_ = self.text_passwords.get()
        Confirm_password = self.text_confpassword.get()

        self.db = Backend.dbconnection.Dbconnect()

        u = Model.User.User(First_name, Last_name, ContactNo, Email_Id, Security_question, Answer, Password_, Confirm_password)

        query = 'delete from rohit_tbl_users where Email_Id = %s'

        values = (u.get_Email_Id(),)

        self.db.insert(query, values)

        messagebox.showinfo('Success', 'selected data deleted successfully')

        self.fetch_data()
        self.clear_data()


    def search_data(self):
        """ Here search button will connected for searching data"""
        global index
        ent = self.text_search.get()
        if ent != "":
            try:
                lis = []
                for row in self.User_tbl.get_children():
                    rows = self.User_tbl.item(row)['values'][0]
                    lis.append(rows)

                search = self.binarysearch(lis, str(self.text_search.get()))
                print(f"search={search}")

                if search:
                    messagebox.showinfo("Success","Found")

                    query = "select * from rohit_tbl_users where contact = %s"
                    values = (search,)
                    rows = self.db.select(query, values)
                    self.User_tbl.delete(*self.User_tbl.get_children())
                    for row in rows:
                        self.User_tbl.insert('', END, values=row)

                else:
                    messagebox.showerror("failed", "Not found")
            except Exception as es:\
                messagebox.showerror("Error",f"Error occurred due to {str(es)}", parent=self.root)

    def binarysearch(self, _list, target):
        start = 1
        end = len(_list) + 1
        while start <= end:
            mid = (start + end) // 2
            mid1 = _list[mid]
            if mid1 < target:
                end = mid - 1
            elif mid1 < target:
                start = mid + 1
            else:
                return mid1

    def sorting(self,events):
        """ Here sorting is for data sorted into ascending & descending order """
        if self.combo_sort.get() == "Ascending":
            query = "select * from rohit_tbl_users;"
            data = self.db.selectall(query)
            sort_val = []
            for values in data:
                sort_val.append(values)
            sorted_val = self.bubblesort_asc(sort_val)
            if len(sorted_val) != 0:
                messagebox.showinfo("Success","Data sorted in ascending order")
                self.User_tbl.delete(*self.User_tbl.get_children())
                for i in sorted_val:
                    self.User_tbl.insert('', END, values=i)
        elif self.combo_sort.get() == "Descending":
            query = "select * from rohit_tbl_users;"
            data = self.db.selectall(query)
            sort_val = []
            for values in data:
                sort_val.append(values)
            sorted_val = self.bubblesort_desc(sort_val)
            if len(sorted_val) != 0:
                messagebox.showinfo("Success","Sorted in Decreasing order")
                self.User_tbl.delete(*self.User_tbl.get_children())
                for i in sorted_val:
                    self.User_tbl.insert('', END, values=i)

    def bubblesort_asc(self, lis):
        for j in range(len(lis) - 1):
            for i in range(len(lis) - 1):
                if lis[i] > lis[i + 1]:
                    lis[i], lis[i + 1] = lis[i + 1], lis[i]
        return lis

    def bubblesort_desc(self, lis):
        for j in range(len(lis) - 1):
            for i in range(len(lis) - 1):
                if lis[i] < lis[i + 1]:
                    lis[i], lis[i + 1] = lis[i + 1], lis[i]
        return lis


# root = Tk()
# ob = View(root)
# root.mainloop()