from models.child import Child
from models.guardian import Guardian
from models.staff_member import StaffMember
from models.room import Room
import repositories.child_repository as child_repository
import repositories.guardian_repository as guardian_repository
import repositories.room_repository as room_repository
import repositories.staff_member_repository as staff_member_repository
import pdb


# pdb.set_trace()

room_1 = Room("oak tree", id = None)
room_repository.save(room_1)
room_2 = Room("maple tree", id = None)
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

child_1 = Child("Adele", 210413, "dairy", guardian_1, room_1, staff_member_1)
child_repository.save(child_1)
child_2 = Child("Paula", 200115, None, guardian_2, room_2, staff_member_2, id = None)
child_repository.save(child_2)
child_3 = Child("Albie", 201020, None, guardian_3, room_1, staff_member_1, id = None)
child_repository.save(child_3)
child_4 = Child("Jack", 180430, "gluten", guardian_2, room_2, staff_member_2, id = None)
child_repository.save(child_4)
child_5 = Child("Doug", 190623, None, guardian_1, room_2, staff_member_2, id = None)
child_repository.save(child_5)
child_6 = Child("Zoe", 220211, "nuts", guardian_3, room_1, staff_member_1, id = None)
child_repository.save(child_6)

# children = child_repository.select_all()
# guardians = guardian_repository.select_all()
# for child in children:
#     print(child.name)  
#     print(child.date_of_birth)  
#     print(child.allergies)  
#     for guardian in guardians:
#         if child.guardian == guardian.id:
#             print(guardian.contact_number)





# result = child_repository.select(34)
# print(result.name)
# child_repository.delete_all()
# child_repository.delete(92)
# child_repository.update()


# guardian_repository.delete_all()
# guardian_repository.select_all()
# guardian_repository.select()
# guardian_repository.delete(43)

result = room_repository.select_all()
print(result[1])
# room_repository.select()

# result_2 = staff_member_repository.select_all()
# print(result_2[0])
# staff_member_repository.select()