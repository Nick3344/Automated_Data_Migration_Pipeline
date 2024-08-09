import sqlite3

conn = sqlite3.connect('source.db')
cursor = conn.cursor()

cursor.execute('''s
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER,
    department TEXT
)
''')

# Sample data
cursor.executemany('''
INSERT INTO employees (name, age, department) VALUES (?, ?, ?)
''', [
    ('Alice', 30, 'HR'),
    ('Bob', 25, 'Engineering'),
    ('Charlie', 35, 'Marketing')
])

# Commit and close
conn.commit()
conn.close()
print("Source database created successfully.")
