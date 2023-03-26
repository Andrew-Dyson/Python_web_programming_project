from db.run_sql import run_sql
from models.staff_member import StaffMember
import repositories.guardian_repository as guardian_repository
import repositories.room_repository as room_repository
import repositories.staff_member_repository as staff_member_repository

def save(staff_member):
    sql = "INSERT INTO staffmembers (name, room_id) VALUES (%s, %s) RETURNING *"
    values = [staff_member.name, staff_member.room.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    staff_member.id = id
    return staff_member


def select_all():
    staff_members = []
    sql = "SELECT * FROM staffmembers"
    results = run_sql(sql)
    for row in results:
        staff_member = StaffMember(row['name'], row['room_id'], row['id'])
        staff_members.append(staff_member)
    return staff_members

def select(id):
    staff_member = None
    sql = "SELECT * FROM staffmembers WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        staff_member = StaffMember(result['name'], result['id'] )
    return staff_member