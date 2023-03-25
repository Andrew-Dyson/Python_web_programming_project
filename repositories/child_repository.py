from db.run_sql import run_sql

from models.child import Child


def save(child):
    sql = "INSERT INTO children(name, date_of_birth, allergies, guardian_id, room_id, staff_member_id) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *"
    values = [child.name, child.date_of_birth, child.allergies, child.guardian.id, child.room.id, child.staff_member.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    child.id = id
    return child

def select_all():

    
def select():

def delete_all():

def delete():
    
def update():
    

