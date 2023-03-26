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

def select_all():
    rooms = []
    sql = "SELECT * FROM rooms"
    results = run_sql(sql)
    for row in results:
        room = Room(row['name'], row['id'])
        rooms.append(room)
    return rooms


def select(id):
    room = None
    sql = "SELECT * FROM rooms WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        room = Room(result['name'], result['id'] )
    return room