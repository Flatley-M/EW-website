import sqlite3

class Database:
    def __init__(self, url):
        with sqlite3.connect(url) as db:
            cursor = db.cursor()
            sql = """
            CREATE TABLE IF NOT EXISTS ew (
                id INTEGER PRIMARY KEY,
                task TEXT NOT NULL,
                subject TEXT,
                beak TEXT,
                dueDate TEXT
            );
            """
            cursor.execute(sql)

            sql_insert = """
            INSERT INTO ew (task, subject, beak, dueDate) VALUES (?, ?, ?, ?);
            """
            cursor.execute(sql_insert, ('Complete Flask web dev', 'Computer Science', 'MC', 'Wednesday'))
            db.commit()


    def get_ews(self, url):
        with sqlite3.connect(url) as db:
            cursor = db.cursor()
            sql_select = "SELECT * FROM ew;"
            cursor.execute(sql_select)
            return cursor.fetchall()

    def create_ew(self, task, subject, beak, dueDate, url):
        with sqlite3.connect(url) as db:
            cursor = db.cursor()
            sql_insert = "INSERT INTO ew (task, subject, beak, dueDate) VALUES (?, ?, ?, ?);"
            cursor.execute(sql_insert, (task, subject, beak, dueDate))
            db.commit()



    # EXTRA CREDIT
    def get_ew(self, id):
        """
        TO IMPLEMENT
        """
        pass