from db.run_sql import run_sql
from models.guardian import Guardian

def save(guardian):
    sql = "INSERT INTO guardians (name, contact_number) VALUES (%s, %s) RETURNING *"
    values = [guardian.name, guardian.contact_number]
    results = run_sql(sql, values)
    id = results[0]['id']
    guardian.id = id
    return guardian
    
def select_all():
    guardians = []
    sql = "SELECT * FROM guardians"
    results = run_sql(sql)
    for row in results:
        guardian = Guardian(row['name'], row['contact_number'], row['id'])
        guardians.append(guardian)
    return guardians


def select(id):
    guardian = None
    sql = "SELECT * FROM guardians WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        guardian = Guardian(result['name'], result['contact_number'], result['id'] )
    return guardian


def delete_all():
    sql = "DELETE FROM guardians"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM GUARDIANS WHERE id = %s"
    values = [id]
    run_sql(sql, values)