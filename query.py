import sqlite3
conn = sqlite3.connect("factbook.db")
query = "SELECT * FROM facts;"
facts = read_sql_