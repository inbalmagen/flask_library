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
    
    # Query to get all books
    cur.execute('SELECT * FROM books')
    books = cur.fetchall()
    
    # Query to get all loans
    cur.execute('''
    SELECT loans.id AS loan_id, users.name AS user_name, books.title AS book_title, 
           loans.loan_date, loans.return_date, loans.due_date 
    FROM loans 
    JOIN users ON loans.user_id = users.id 
    JOIN books ON loans.book_id = books.id
    ''')
    loans = cur.fetchall()
    
    db.close()
    
    return render_template('index.html', books=books, loans=loans)

if __name__ == '__main__':
    app.run(debug=True)
