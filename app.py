from flask import Flask, render_template, request, redirect
from db import Database

app = Flask(__name__)
db = Database('database.db')


@app.route('/')
def list_ews():
    ews = db.get_ews('database.db')
    return render_template('list.html', ews = ews)

@app.route('/add', methods=['POST'])
def add_ew():
    task = request.form.get('task')
    subject = request.form.get('subject')
    beak = request.form.get('beak')
    dueDate = request.form.get('dueDate')
    if task:
        db.create_ew(task, subject, beak, dueDate, 'database.db')
        return redirect('/')

# EXTRA CREDIT
@app.route('/<int:id>')
def view_ew(id):
    """
    TO IMPLEMENT
    """
    pass