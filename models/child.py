from datetime import *

class Child:
    def __init__(self, name, date_of_birth, allergies, guardian, room, staff_member, childs_age = None, id = None):
        self.name = name
        self.date_of_birth = date_of_birth
        self.allergies = allergies
        self.guardian = guardian
        self.room = room
        self.staff_member = staff_member
        self.childs_age = childs_age
        self.id = id


    def convert_date_of_birth(self):
        return (datetime.fromisoformat(self.date_of_birth))


    def calculate_age_years_months(self, date_of_birth):
        date_today = date.today()
        
        if date_today.month < date_of_birth.month:
            age_in_months = (date_today.month - date_of_birth.month) + 12
        elif date_today.month > date_of_birth.month:
            age_in_months = (date_today.month - date_of_birth.month)

        if (date_today.month > date_of_birth.month) and (date_today.year - date_of_birth.year > 0):
            age_in_years = (date_today.year - date_of_birth.year)
        elif (date_today.month < date_of_birth.month) and (date_today.year - date_of_birth.year == 1):
            age_in_years = 0
        elif (date_today.month < date_of_birth.month) and (date_today.year - date_of_birth.year > 1):
            age_in_years = (date_today.year - date_of_birth.year) - 1
        else:
            age_in_years = 0

        if age_in_years == 1:
            result = f"{age_in_years} year old"
        elif age_in_years > 1:
            result = f"{age_in_years} years old"
        else:
            result = f"{age_in_months} months old"
        return result  





