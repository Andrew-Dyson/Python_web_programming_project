import unittest

from models.child import *
from models.guardian import Guardian
from models.room import Room
from models.staff_member import StaffMember
from datetime import *


class TestChild(unittest.TestCase):
    def setUp(self):
        self.room_1 = Room("Oak tree", id = None)
        self.guardian_1 = Guardian("John", "06957483746", id = None)   
        self.staff_member_1 = StaffMember("Bethan", self.room_1, id = None)
        self.child_1 = Child("Tom", "2021-04-13", "dairy", self.guardian_1, self.room_1, self.staff_member_1, id = None)

    def test_child_has_name(self):
        self.assertEqual("Tom", self.child_1.name)


    def test_child_has_an_age_less_than_year(self):
        room_1 = Room("Oak tree", id = None)
        guardian_1 = Guardian("John", "06957483746", id = None)   
        staff_member_1 = StaffMember("Bethan", room_1, id = None)
        child_1 = Child("Adele", "2022-04-13", "dairy", guardian_1, room_1, staff_member_1)
        DOB = child_1.convert_date_of_birth()
        age = child_1.calculate_age_years_months(DOB)
        self.assertEqual("11 months old", age)

    def test_child_has_an_age_of_one_year(self):
        room_1 = Room("Oak tree", id = None)
        guardian_1 = Guardian("John", "06957483746", id = None)   
        staff_member_1 = StaffMember("Bethan", room_1, id = None)
        child_1 = Child("Adele", "2021-04-13", "dairy", guardian_1, room_1, staff_member_1)
        DOB = child_1.convert_date_of_birth()
        age = child_1.calculate_age_years_months(DOB)
        self.assertEqual("1 year old", age)

    def test_child_has_an_age_two_years_old(self):
        room_1 = Room("Oak tree", id = None)
        guardian_1 = Guardian("John", "06957483746", id = None)   
        staff_member_1 = StaffMember("Bethan", room_1, id = None)
        child_1 = Child("Adele", "2021-01-13", "dairy", guardian_1, room_1, staff_member_1)
        DOB = child_1.convert_date_of_birth()
        age = child_1.calculate_age_years_months(DOB)
        self.assertEqual("2 years old", age)

    def test_child_has_an_age_older_than_two_years_old(self):
        room_1 = Room("Oak tree", id = None)
        guardian_1 = Guardian("John", "06957483746", id = None)   
        staff_member_1 = StaffMember("Bethan", room_1, id = None)
        child_1 = Child("Adele", "2017-01-13", "dairy", guardian_1, room_1, staff_member_1)
        DOB = child_1.convert_date_of_birth()
        age = child_1.calculate_age_years_months(DOB)
        self.assertEqual("6 years old", age)