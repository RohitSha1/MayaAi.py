
class User:
    def __init__(self, text_fname, text_lname, text_contact, text_email,
                 cmb_quest, text_Answer, text_passwords, text_confpassword):

        self.__First_name = text_fname
        self.__Last_name = text_lname
        self.__contact = text_contact
        self.__Email_Id = text_email
        self.__Security_question = cmb_quest
        self.__Answer = text_Answer
        self.__Password_ = text_passwords
        self.__Confirm_password = text_confpassword

    def set_First_name(self, text_fname):
        self.__First_name = text_fname

    def get_First_name(self):
         return self.__First_name

    def set_Last_name(self, text_lname):
        self.__Last_name = text_lname

    def get_Last_name(self):
        return self.__Last_name

    def set_contact(self, text_contact):
        self.__contact = text_contact

    def get_contact(self):
        return self.__contact

    def set_Email_Id(self,text_email):
        self.__Email_Id = text_email

    def get_Email_Id(self):
        return self.__Email_Id

    def set_Security_question(self, cmb_quest):
        self.__Security_question = cmb_quest

    def get_Security_question(self):
        return self.__Security_question

    def set_Answer(self, text_Answer):
        self.__Answer = text_Answer

    def get_Answer(self):
        return self.__Answer

    def set_Password_(self, text_passwords):
        self.__Password_ = text_passwords

    def get_Passwords(self):
        return self.__Password_

    def set_Confirm_password(self, text_confpassword):
        self.__Confirm_password = text_confpassword

    def get_Confirm_password(self):
        return self.__Confirm_password

