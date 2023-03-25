from db.run_sql import run_sql
from models.room import Room


def save(room):
    sql = "INSERT INTO rooms (name) VALUES (%s) RETURNING *"
    values = [room.name]
    results = run_sql(sql, values)
    print(results)
    id = results[0]['id']
    room.id = id
    return room