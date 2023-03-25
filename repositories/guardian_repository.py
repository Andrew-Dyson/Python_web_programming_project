from db.run_sql import run_sql
from models.guardian import Guardian

def save(guardian):
    sql = "INSERT INTO guardians (name, contact_number) VALUES (%s, %s) RETURNING *"
    values = [guardian.name, guardian.contact_number]
    results = run_sql(sql, values)
    id = results[0]['id']
    guardian.id = id
    return guardian
    