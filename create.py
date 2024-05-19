import sqlite3

# Data to be inserted
data = [
    (16, 'QwiK'),
    (50, 'Pan'),
    (1, 'Vivid'),
    (0, 'Who.SOLR'),
    (32, 'Ikariii'),
    (1, 'Bentley'),
    (0, 'LonelyValentine'),
    (69, 'Takito'),
    (0, 'Fuecoco42'),
    (2, 'Codiak'),
    (0, 'Blabbbb'),
    (0, 'M4p13'),
    (12, 'BLADE.VGS'),
    (0, 'Arronnite'),
    (2, 'Hssonger'),
    (0, 'arshiaarta'),
    (0, 'Butter-'),
    (0, 'Stun'),
    (57, 'Nat1x'),
    (0, 'Sneaki'),
    (0, 'TOXIC'),
    (0, 'Tyson_07'),
    (0, 'III7Toast'),
    (0, 'SVG10'),
    (44, 'Basilmaz'),
    (0, 'Epaza'),
    (0, 'Micro'),
    (0, 'RICHDGEB'),
    (0, 'Malicious Panda'),
    (0, 'Ares.VGS'),
    (0, 'Sleepy'),
    (0, 'Clubcracker'),
    (0, 'IAmPancake'),
    (0, 'ice'),
    (0, 'Pulpos43'),
    (31, 'ryze'),
]

# Connect to the database
conn = sqlite3.connect('standings.db')
c = conn.cursor()

# Clear existing data
c.execute('DELETE FROM standings')

# Insert new data
c.executemany('INSERT INTO standings (points, team) VALUES (?, ?)', data)

conn.commit()
conn.close()
