from db.run_sql import run_sql
from models.staff_member import StaffMember

def save(staff_member):
    sql = "INSERT INTO staffmembers (name) VALUES (%s) RETURNING *"
    values = [staff_member.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    staff_member.id = id
    return staff_member
