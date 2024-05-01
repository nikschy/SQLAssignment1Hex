import sqlite3

db = sqlite3.connect(":memory:")

cursor = db.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS AGES(
  NAME VARCHAR(128),
  AGE INTEGER
)''')


cursor.execute('''DELETE FROM AGES''')

cursor.execute('''INSERT INTO AGES (NAME,AGE) VALUES('Mara',28)''')
cursor.execute('''INSERT INTO AGES (NAME,AGE) VALUES('Otto',33)''')
cursor.execute('''INSERT INTO AGES (NAME,AGE) VALUES('Fyn',31)''')
cursor.execute('''INSERT INTO AGES (NAME,AGE) VALUES('Neshawn',17)''')


cursor.execute('''SELECT HEX(NAME||AGE) AS X FROM AGES ORDER BY X''')


user1 = cursor.fetchone()
print("The first row in the resulting record set: " + user1[0])

db.commit()
db.close()