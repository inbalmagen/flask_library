from flask import Flask, render_template
import sqlite3

app = Flask(__name__)
DATABASE = 'library.db'

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    db = get_db()
    cur = db.cursor()
    cur.execute('SELECT * FROM books')
    books = cur.fetchall()
    db.close()
    return render_template('index.html', books=books)

if __name__ == '__main__':
    app.run(debug=True)
