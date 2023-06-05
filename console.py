from models.child import Child
from models.guardian import Guardian
from models.staff_member import StaffMember
from models.room import Room
import repositories.child_repository as child_repository
import repositories.guardian_repository as guardian_repository
import repositories.room_repository as room_repository
import repositories.staff_member_repository as staff_member_repository
import pdb
import datetime

# pdb.set_trace()

room_1 = Room("Oak tree", id = None)
room_repository.save(room_1)
room_2 = Room("Maple tree", id = None)
room_repository.save(room_2)

guardian_1 = Guardian("John", "06957483746", id = None)
guardian_repository.save(guardian_1)
guardian_2 = Guardian("Olivia", "06758463726", id = None)
guardian_repository.save(guardian_2)
guardian_3 = Guardian("Victor", "08493672834", id = None)
guardian_repository.save(guardian_3)

staff_member_1 = StaffMember("Bethan", room_1, id = None)
staff_member_repository.save(staff_member_1)
staff_member_2 = StaffMember("Elliot", room_2, id = None)
staff_member_repository.save(staff_member_2)

child_1 = Child("Adele", "2021-04-13", "dairy", guardian_1, room_1, staff_member_1, id = None)
child_repository.save(child_1)
child_2 = Child("Paula", "2020-01-15", "none", guardian_2, room_2, staff_member_2, id = None)
child_repository.save(child_2)
child_3 = Child("Albie", "2020-10-20", "none", guardian_3, room_1, staff_member_1, id = None)
child_repository.save(child_3)
child_4 = Child("Jack", "2018-04-30", "gluten", guardian_2, room_2, staff_member_2, id = None)
child_repository.save(child_4)

