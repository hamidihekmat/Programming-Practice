import sqlite3

conn = sqlite3.connect('employee.db')

c = conn.cursor()

# c.execute("""CREATE TABLE employee (
#                 first text,
#                 last text,
#                 pay integer
#                 )""")

c.execute("INSERT INTO employee VALUES ('Hekmat', 'Hamidi', 50000)")

conn.commit()
conn.close()
