import sqlite3

# Connect to the destination database (creates a new one if it doesn't exist)
conn = sqlite3.connect('destination.db')
cursor = conn.cursor()

# Create a similar table in the destination database
cursor.execute('''
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER,
    department TEXT
)
''')

# Commit and close
conn.commit()
conn.close()
print("Destination database created successfully.")
