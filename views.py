from flask import flash, render_template, request, redirect, session, url_for, send_from_directory, jsonify
from app import app

# @app.route('/')
# def index():
#     return render_template('A01.html')

#? ---------- A01:2021-Broken Access Control ----------

@app.route('/A01_overview')
def a01_overview():
    return render_template('a01/overview.html', title='A01:2021-Broken Access Control')
# redirect(url_for('a01_example'))

@app.route('/A01_example')
def a01_example():
    return render_template('a01/example.html')

@app.route('/A01_howprevent')
def a01_howprevent():
    return render_template('a01/howprevent.html')

#criar links dinamicos  com A01/Variavel