import sqlite3

# Data to be inserted into the standings table
team_data = [
    ('QwiK', 19), ('Pan', 55), ('Vivid', 1), ('Who.SOLR', 2), ('Ikariii', 32),
    ('Bentley', 5), ('LonelyValentine', 0), ('Takito', 84), ('Fuecoco42', 0),
    ('Codiak', 17), ('Blabbbb', 0), ('M4p13', 0), ('BLADE.VGS', 12), ('Arronnite', 0),
    ('Hssonger', 2), ('arshiaarta', 0), ('Butter-', 0), ('Stun', 0), ('Nat1x', 67),
    ('Sneaki', 0), ('TOXIC', 0), ('Tyson_07', 0), ('III7Toast', 0), ('SVG10', 0),
    ('Basilmaz', 54), ('Epaza', 6), ('Micro', 7), ('RICHDGEB', 0), ('Malicious Panda', 4),
    ('Ares.VGS', 0), ('Sleepy', 0), ('Clubcracker', 0), ('IAmPancake', 0), ('ice', 0),
    ('Pulpos43', 0), ('ryze', 31)
]

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('standings.db')
cursor = conn.cursor()

# Drop the standings table if it exists
cursor.execute('DROP TABLE IF EXISTS standings')

# Create the standings table
cursor.execute('''
    CREATE TABLE standings (
        team TEXT PRIMARY KEY,
        points INTEGER
    )
''')

# Insert the team standings
cursor.executemany('INSERT INTO standings (team, points) VALUES (?, ?)', team_data)

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Team standings updated successfully.")
