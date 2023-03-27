from flask import Blueprint, Flask, redirect, render_template, request
from models.child import Child
from models.guardian import Guardian
from models.staff_member import StaffMember
from models.room import Room
import repositories.child_repository as child_repository
import repositories.guardian_repository as guardian_repository
import repositories.room_repository as room_repository
import repositories.staff_member_repository as staff_member_repository
import pdb

children_blueprint = Blueprint("children", __name__)


@children_blueprint.route("/children")
def children():
    children = child_repository.select_all()
    guardians = guardian_repository.select_all()
    return render_template("children/children.html", children = children, guardians = guardians)

@children_blueprint.route("/children/delete/<id>", methods=['POST'])
def remove_child(id):
    child_repository.delete(id)
    return redirect("/children")

@children_blueprint.route("/new", methods=['GET'])
def new_child():
    guardians = guardian_repository.select_all()
    rooms = room_repository.select_all()
    staff_members = staff_member_repository.select_all()
    return render_template("new/new.html", guardians = guardians, rooms = rooms, staff_members = staff_members)


@children_blueprint.route("/children/register", methods=['POST'])
def register_child():
    name = request.form['name']
    date_of_birth = int(request.form['date_of_birth'])
    allergies = request.form['allergies']
    guardian_id = request.form['guardian_id']
    guardian = guardian_repository.select(guardian_id)
    staff_members = staff_member_repository.select_all()
    rooms = room_repository.select_all()
    if date_of_birth <= 200830:
        staff_member = staff_members[0]
        room = rooms[0]
    else:
        staff_member = staff_members[1]
        room = rooms[1]
    new_child = Child(name, date_of_birth, allergies, guardian, room, staff_member)
    child_repository.save(new_child)
    return redirect("/children")


@children_blueprint.route("/edit/<id>", methods=['GET'])
def edit_child(id):
    child = child_repository.select(id)
    guardians = guardian_repository.select_all()
    rooms = room_repository.select_all()
    staff_members = staff_member_repository.select_all()
    return render_template("edit/edit.html", child = child, guardians = guardians, rooms = rooms, staff_members = staff_members)

@children_blueprint.route("/<id>/edit", methods=['POST'])
def update_child(id):
    name = request.form['name']
    date_of_birth = int(request.form['date_of_birth'])
    allergies = request.form['allergies']
    guardian_id = request.form['guardian_id']
    guardian = guardian_repository.select(guardian_id)
    staff_members = staff_member_repository.select_all()
    rooms = room_repository.select_all()
    if date_of_birth <= 200830:
        staff_member = staff_members[0]
        room = rooms[0]
    else:
        staff_member = staff_members[1]
        room = rooms[1]
    new_child = Child(name, date_of_birth, allergies, guardian, room, staff_member)
    child_repository.save(new_child)
    return redirect("/children")
    