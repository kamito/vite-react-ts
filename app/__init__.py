from flask import request, session, render_template, redirect, jsonify
from .app import app

@app.route("/")
def top():
    return render_template("top.html")
