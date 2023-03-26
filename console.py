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

# room_1 = Room("oak tree", id = None)
# room_repository.save(room_1)
# room_2 = Room("maple tree", id = None)
# room_repository.save(room_2)

# guardian_1 = Guardian("John", "86957483746", id = None)
# guardian_repository.save(guardian_1)
# guardian_2 = Guardian("Olivia", "86758463726", id = None)
# guardian_repository.save(guardian_2)
# guardian_3 = Guardian("Victor", "78493672834", id = None)
# guardian_repository.save(guardian_3)

# staff_member_1 = StaffMember("Bethan", room_1, id = None)
# staff_member_repository.save(staff_member_1)
# staff_member_2 = StaffMember("Elliot", room_2, id = None)
# staff_member_repository.save(staff_member_2)

# child_1 = Child("Adele", "130421", "dairy", guardian_1, room_1, staff_member_1)
# print(child_1.staff_member.id)
# child_repository.save(child_1)
# child_2 = Child("Paula", "150120", None, guardian_2, room_2, staff_member_2, id = None)
# child_repository.save(child_2)
# child_3 = Child("Albie", "201020", None, guardian_3, room_1, staff_member_1, id = None)
# child_repository.save(child_3)
# child_4 = Child("Jack", "300418", "gluten", guardian_2, room_2, staff_member_2, id = None)
# child_repository.save(child_4)
# child_5 = Child("Doug", "230619", None, guardian_1, room_2, staff_member_2, id = None)
# child_repository.save(child_5)
# child_6 = Child("Zoe", "110222", "nuts", guardian_3, room_1, staff_member_1, id = None)
# child_repository.save(child_6)

# child_repository.select_all()
# result = child_repository.select(34)
# print(result.name)
# child_repository.delete_all()
# child_repository.delete()
# child_repository.update()


# guardian_repository.delete_all()
# guardian_repository.select_all()
# guardian_repository.select()
guardian_repository.delete(43)

# room_repository.select_all()
# room_repository.select()

# staff_member_repository.select_all()
# staff_member_repository.select()