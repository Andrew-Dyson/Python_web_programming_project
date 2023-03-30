from db.run_sql import run_sql

from models.child import Child
from models.child import *
import repositories.guardian_repository as guardian_repository
import repositories.room_repository as room_repository
import repositories.staff_member_repository as staff_member_repository



def save(child):
    sql = "INSERT INTO children(name, date_of_birth, allergies, guardian_id, room_id, staff_member_id, childs_age) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING *"
    DOB = child.convert_date_of_birth()
    childs_age = child.calculate_age_years_months(DOB)
    values = [child.name, child.date_of_birth, child.allergies, child.guardian.id, child.room.id, child.staff_member.id, childs_age]
    results = run_sql(sql, values)
    id = results[0]['id']
    child.id = id
    return child


def select_all():
    children = []
    sql = "SELECT * FROM children"
    results = run_sql(sql)
    for row in results:
        child = Child(row['name'], row['date_of_birth'], row['allergies'], row['guardian_id'], row['room_id'], row['staff_member_id'], row['childs_age'], row['id'])
        children.append(child)
    return children


def select(id):
    sql = "SELECT * FROM children WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    

    if len(results) > 0:
        selected_child = results[0]
        guardian = guardian_repository.select(selected_child['guardian_id'])
        room = room_repository.select(selected_child['room_id'])
        staff_member = staff_member_repository.select(selected_child['staff_member_id'])
        child = Child(selected_child['name'], selected_child['date_of_birth'], selected_child['allergies'], guardian, room, staff_member, selected_child['id'])
    return child


def delete_all():
    sql = "DELETE FROM children"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM children WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)
    
def update(child):
    # DOB = child.convert_date_of_birth()
    # childs_age = child.calculate_age_years_months(DOB)
    
    sql = "UPDATE children SET (name, date_of_birth, allergies, guardian_id, room_id, staff_member_id, childs_age) = (%s, %s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [child.name, child.date_of_birth, child.allergies, child.guardian.id, child.room.id, child.staff_member.id, child.id]
    run_sql(sql, values)

    # sql = "UPDATE children SET (name, date_of_birth, allergies, guardian_id) = (%s, %s, %s, %s) WHERE id = %s"
    # values = [child.name, child.date_of_birth, child.allergies, child.guardian.id, child.id]
    # run_sql(sql, values)

