
import unittest
from Backend.dbconnection import Dbconnect


class TestConnection(unittest.TestCase):
    def setUp(self):
        self.db = Dbconnect()
        self.values = (1, 'san', 'san@gmail.com')

    def test_create_db(self):
        query = "create database test_Algorithm"
        actual = self.db.create(query)
        self.assertIsNone(actual)

    def test_create_tbl(self):
        use_db_query = "use test_Algorithm"
        exe_db_query = self.db.create(use_db_query)
        self.assertIsNone(exe_db_query)
        query = "create table test_User(test_roll_no int NOT NULL, test_name varchar(40), test_email " \
                "varchar(50));"
        actual = self.db.create(query)
        self.assertIsNone(actual)

    def test_insert_student_data(self):
        use_db_query = "use test_Algorithm"
        exe_db_query = self.db.create(use_db_query)
        self.assertIsNone(exe_db_query)
        query1 = "insert into test_User(test_roll_no, test_name, test_email) values (%s,%s,%s)"
        self.db.insert(query1, self.values)
        query2 = "select * from test_User where test_roll_no = 1"
        actual = self.db.selectall(query2)
        expected = [(1, 'san', 'san@gmail.com'),]
        self.assertEqual(expected, actual)