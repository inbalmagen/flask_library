import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('library.db')

# Create a cursor object
cur = conn.cursor()

# Create the books table with an image field
cur.execute('''
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    isbn TEXT UNIQUE NOT NULL,
    published_date TEXT,
    genre TEXT,
    image_url TEXT, -- URL to the book's image
    available INTEGER DEFAULT 1
)
''')

# Create the users table
cur.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    phone TEXT,
    join_date TEXT DEFAULT CURRENT_DATE
)
''')

# Create the loans table
cur.execute('''
CREATE TABLE IF NOT EXISTS loans (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    book_id INTEGER NOT NULL,
    loan_date TEXT DEFAULT CURRENT_DATE,
    return_date TEXT,
    due_date TEXT,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (book_id) REFERENCES books(id)
)
''')

# Insert data into the books table
cur.execute("INSERT INTO books (title, author, isbn, published_date, genre, image_url) VALUES (?, ?, ?, ?, ?, ?)",
            ('1984', 'George Orwell', '9780451524935', '1949-06-08', 'Dystopian', 'https://cdn.waterstones.com/bookjackets/large/9780/1410/9780141036144.jpg'))

cur.execute("INSERT INTO books (title, author, isbn, published_date, genre, image_url) VALUES (?, ?, ?, ?, ?, ?)",
            ('To Kill a Mockingbird', 'Harper Lee', '9780061120084', '1960-07-11', 'Fiction', 'https://cdn.britannica.com/21/182021-050-666DB6B1/book-cover-To-Kill-a-Mockingbird-many-1961.jpg'))

# Insert data into the users table
cur.execute("INSERT INTO users (name, email, phone) VALUES (?, ?, ?)",
            ('John Doe', 'john@example.com', '123-456-7890'))

cur.execute("INSERT INTO users (name, email, phone) VALUES (?, ?, ?)",
            ('Jane Smith', 'jane@example.com', '098-765-4321'))

# Insert data into the loans table
cur.execute("INSERT INTO loans (user_id, book_id, due_date) VALUES (?, ?, ?)",
            (1, 1, '2024-08-30'))

cur.execute("INSERT INTO loans (user_id, book_id, due_date) VALUES (?, ?, ?)",
            (2, 2, '2024-08-31'))

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Database created and data inserted successfully!")
