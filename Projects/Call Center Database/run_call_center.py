# Runs call_center.sql and shows the results
# Run:  python run_call_center.py
# (Nothing to install. sqlite3 comes with Python.)

import sqlite3

conn = sqlite3.connect("call_center.db")
cur = conn.cursor()

# Remove old tables so the program can be run again and again
cur.execute("DROP TABLE IF EXISTS calls")
cur.execute("DROP TABLE IF EXISTS agents")

# Read the SQL file and split it into separate statements at each ;
text = open("call_center.sql").read()
statements = text.split(";")

for statement in statements:
    lines = statement.strip().split("\n")

    title = ""
    sql = ""
    for line in lines:
        if line.startswith("--"):
            title = line          # remember the comment as the title
        else:
            sql = sql + line + "\n"

    sql = sql.strip()
    if sql == "":
        continue

    cur.execute(sql)

    # If it is a SELECT, show the result
    if sql.startswith("SELECT"):
        print("\n" + title)
        names = []
        for column in cur.description:
            names.append(column[0])
        print(names)
        for row in cur.fetchall():
            print(row)

conn.commit()
conn.close()
print("\nDone! The database is saved as call_center.db")
