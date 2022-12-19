from flask import flash, render_template, request, redirect, session, url_for, send_from_directory, jsonify
from app import app

@app.route('/')
def index():
    return render_template('A01.html')