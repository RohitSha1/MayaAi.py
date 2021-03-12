
import unittest
from Model import User


class Test_register(unittest.TestCase):
    def setUp(self):
        self.e1 = User.User("Po2tato", "a12", "982376", "banana1@gmail.com", "Lahan2", "ramya69", "564789", "564789")

    def test_set_First_name(self):
        self.e1.set_First_name("Po2tato")
        self.assertEqual("Po2tato", self.e1.get_First_name())

    def test_get_First_name(self):
        self.assertEqual("Po2tato", self.e1.get_First_name())

    def test_set_Last_name(self):
        self.e1.set_Last_name("a12")
        self.assertEqual("a12", self.e1.get_Last_name())

    def test_get_Last_name(self):
        self.assertEqual("a12", self.e1.get_Last_name())

    def test_set_contact(self):
        self.e1.set_contact("982376")
        self.assertEqual("982376", self.e1.get_contact())

    def test_get_contact(self):
        self.assertEqual("982376", self.e1.get_contact())

    def test_set_Email_Id(self):
        self.e1.set_Email_Id("banana1@gmail.com")
        self.assertEqual("banana1@gmail.com", self.e1.get_Email_Id())

    def test_get_Email_Id(self):
        self.assertEqual("banana1@gmail.com", self.e1.get_Email_Id())

    def test_set_Security_question(self):
        self.e1.set_Security_question("Lahan2")
        self.assertEqual("Lahan2", self.e1.get_Security_question())

    def test_get_Security_question(self):
        self.assertEqual("Lahan2", self.e1.get_Security_question())

    def test_set_Answer(self):
        self.e1.set_Answer("ramya69")
        self.assertEqual("ramya69", self.e1.get_Answer())

    def test_get_Answer(self):
        self.assertEqual("ramya69", self.e1.get_Answer())

    def test_set_Password(self):
        self.e1.set_Password_("564789")
        self.assertEqual("564789", self.e1.get_Passwords())
    #
    def test_get_Password(self):
        self.assertEqual("564789", self.e1.get_Passwords())

    def tearDown(self):
        self.e1 = None
