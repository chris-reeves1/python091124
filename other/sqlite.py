import sqlite3

# better to use 'with'

#conn = sqlite3.connect("example.db")
#c = conn.cursor()

# commands 
# CREATE - creates a new table
# INSERT - insert data into a table
# SELECT - query data from the table
# UPDATE - modify the data
# DELETE - remove data
# WHERE - filtering

# CREATE

#c.execute("""
 #   CREATE TABLE IF NOT EXISTS students (
  #  id INTEGER PRIMARY KEY,
  #  name TEXT NOT NULL,
  #  age INTEGER,
   # grade TEXT
   # )
#""")

#conn.commit() # save the changes

# insert data
# ? - placeHolder - use this rather than calling variables. 
# safer!! 

#c.execute("SELECT * FROM students WHERE name = ? AND age = ? AND grade = ?", ("chris", 40, "A"))
#if c.fetchone() is None:
  #  c.execute("""
 #       INSERT INTO students (name, age, grade)
  #      VALUES (?, ?, ?)
    """, ("chris", 40, "A"))
 #   conn.commit()
#else:
 #   print("already in the db")

# Update 

#c.execute("""
    #UPDATE students
   # SET grade = ?
   # WHERE name = ?
""", ("B", "chris"))
#conn.commit()

# query

#c.execute("SELECT * FROM students")
#x = c.fetchall()

#for data in x:
#    print(data)

# delete

#c.execute("""
  #  DELETE FROM students
 #   WHERE name = ?
#""", ("chris",))
#conn.commit()

# query

#c.execute("SELECT * FROM students")
#x = c.fetchall()

#for data in x:
#    print(data)

# execute many

#students_data = [
  #  ("person1", 22, "A"),
 #   ("person2", 30, "B"),
 #   ("person3", 60, "A")
#] 

#c.executemany("""
#    INSERT INTO students (name, age, grade)
#    VALUES (?, ?, ?)
#""", students_data)
#conn.commit()

# query

#c.execute("SELECT * FROM students")
#x = c.fetchall()

#for data in x:
    #print(data)




# library database
# Creata a table calle books:
# books: - id, title, author, year, available
# insert data: at least 3 entries.
# Query all data
# filter by a specific author. 
# updata a book to be unavailable,
# delete a book. 