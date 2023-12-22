import sqlite3

# Create a connection to the DB
connection_manager = sqlite3.connect("users.db")

# Create a cursor object
my_cursor = connection_manager.cursor()

# Create a new table
my_cursor.execute("CREATE TABLE IF NOT EXISTS  (Mr./Ms.,First Name, Last Name, Age ,Address)")

query_string = """
INSERT INTO users VALUES (?,?,?,?,?)
"""