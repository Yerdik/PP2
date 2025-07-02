import psycopg2
import csv

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="bestPw03!"
)

current = conn.cursor()
create_table = '''
CREATE TABLE phonebook(
   name varchar,
   phone varchar
)
'''
insert = '''
INSERT INTO phonebook VALUES(%s, %s);
'''
select = '''
SELECT name FROM phonebook;
'''
update = '''
UPDATE phonebook SET phone = %s WHERE name =%s;
'''
delete = '''
DELETE FROM phonebook WHERE name=%s;
'''
# current.execute(create_table)
command = input()
if command == "insert":
    current.execute(insert, (input(), input()))
elif command == "update":
    current.execute(update, (input(), input()))
elif command == "delete":
    current.execute(delete, [input()])
elif command == "csv":
    with open('phonebook.csv', 'r') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            current.execute(insert, row)

current.execute(select)
s = current.fetchall()
print(s)

current.close()
conn.commit()
conn.close()