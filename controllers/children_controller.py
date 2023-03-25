from flask import Blueprint, Flask, redirect, render_template, request


children_blueprint = Blueprint("children", __name__)