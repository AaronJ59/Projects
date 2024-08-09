import sqlite3
conn = sqlite3.connect("verses.db")
cur = conn.cursor()


query = '''INSERT INTO verses (emotion, verse, reference) VALUES (?, ?, ?)'''
data = ('', "", '')

cur.execute(query, data)

conn.commit()
conn.close()
