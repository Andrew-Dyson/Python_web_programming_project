from db.run_sql import run_sql
from models.staff_member import StaffMember

def save(staff_member):
    sql = "INSERT INTO staffmembers (name) VALUES (%s) RETURNING *"
    values = [staff_member.name]
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