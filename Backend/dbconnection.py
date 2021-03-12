
import mysql.connector

class Dbconnect:
    def __init__(self):
        self.con = mysql.connector.connect(host='localhost', user='root', password='Qbit1001', database='aimaya',
                                           auth_plugin='mysql_native_password')
        self.cursor = self.con.cursor()

    def insert(self, query, values):
        self.cursor.execute(query, values)
        self.con.commit()

    def update(self, query, values):
        self.cursor.execute(query, values)
        self.con.commit()

    def delete(self, query, values):
        self.cursor.execute(query, values)
        self.con.commit()

    def select(self, query, values):
        self.cursor.execute(query, values)
        rows = self.cursor.fetchall()
        self.con.commit()
        return rows

    def selectall(self, query):
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        self.con.commit()
        return rows

    def create(self, query):
        self.cursor.execute(query)
        self.con.commit()
    #
    # def close(self):
    #     if self.con:
    #         self.con.commit()
    #         self.con.close()

    # def delete(self, values):
    #     query = 'delete from rohit_tbl_users where Email_id = %s'
    #     try:
    #         values = (values,)
    #         self.cursor.execute(query, values)
    #         self.con.commit()
    #         return True
    #     except Exception:
    #         return False


    # def __del__(self):
    #     self.con.commit()
    #     if self.cursor:
    #         self.cursor.close()
    #     if self.con:
    #         self.con.close()
