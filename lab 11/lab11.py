import psycopg2
import csv
import re

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="yerdik890"
)

current = conn.cursor()
create_table = '''
CREATE TABLE phonebook(
   name varchar,
   phone varchar
)
'''

search = '''
CREATE OR REPLACE FUNCTION getT(getname VARCHAR)
   RETURNS TABLE (
      id INT,
      name VARCHAR,
      number VARCHAR
)
AS $$
BEGIN
   RETURN QUERY SELECT * FROM phonebook WHERE phonebook.name ILIKE getname OR phonebook.phone ILIKE getname;
END; $$
LANGUAGE PLPGSQL; 

SELECT * FROM getT (%s); 
'''

update = '''
CREATE OR REPLACE PROCEDURE insertT(
   getname VARCHAR,
   getphone VARCHAR
)
AS $$
BEGIN 
   IF EXISTS (SELECT * FROM phonebook WHERE name = getname) THEN
      UPDATE Phonebook SET phone = getphone WHERE name = getname;
   ELSE
      INSERT INTO phonebook VALUES(name, phone);
   END IF;
END; $$
LANGUAGE PLPGSQL;

CALL insertT(%s, %s);
'''
delete = '''
CREATE OR REPLACE PROCEDURE deleteT(getname VARCHAR)
AS $$
BEGIN
   DELETE FROM Phonebook WHERE phonebook.name = getname OR phonebook.phone = getname;
END; $$

LANGUAGE PLPGSQL;

CALL deleteT(%s);
'''
pagination = '''
SELECT * FROM phonebook ORDER BY phonebook.id LIMIT %s OFFSET %s
'''
def check(s): 
    return bool(re.match(r"[\+\d]?(\d{2,3}[-\.\s]??\d{2,3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})", s))
while True: 
   command = input("search, iou, insert, pagination, delete, exit\n") 
# current.execute(create_table)
   if command == "search":
      n = input()
      word = "%" + n + "%"
      current.execute(search, [word])
      print(*current.fetchall(), sep='\n')
   elif command == 'iou':
      name = input("Введите имя: ")
      phone_number = input("Введите номер: ")
      current.execute(update, (name, phone_number))
      conn.commit()
   elif command == "delete":
      name = input("Введите имя которое нужно удалить: ")
      current.execute(delete, [name])
      conn.commit()
   elif command == 'insert': 
        with open("phoneBookk.csv", "r") as f: 
            reader = csv.reader(f, delimiter=",") 
            for row in reader: 
                if check(row[3]): 
                    current.execute(update, row) 
                else: 
                    print(*row) 
            conn.commit() 
   elif command == 'pagination':
      a, b = map(int, input("LIMIT, OFFSET: ").split())
      current.execute(pagination, (a, b))
      print(*current.fetchall(), sep='\n')
   elif command == 'exit': 
         break 

current.close()
conn.commit()
conn.close()
