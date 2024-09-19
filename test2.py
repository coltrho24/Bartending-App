import sqlite3

conn = sqlite3.connect(r'C:\Program Files\SQLiteStudio\Drinks')
c = conn.cursor()
c.execute('SELECT column10, column11, column12, column13, column14, column15, column16, column17, column18 FROM Drinks')

rows = c.fetchall()

for row in rows:
    print(row)

conn.close()