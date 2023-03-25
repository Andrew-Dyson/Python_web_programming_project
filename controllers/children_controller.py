# from flask import Flask, Blueprint, render_template, request, redirect



# children_blueprint = Blueprint("children", __name__)


from flask import redirect, request, render_template

from app import app

@app.route("/")
def index():
    return render_template("index.html")