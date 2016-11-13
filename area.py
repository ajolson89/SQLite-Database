import sqlite3
import pandas

conn = sqlite3.connect("factbook.db")
query = 'SELECT SUM(area_land) FROM facts WHERE area_land != "" ;'
query2 = 'SELECT SUM(area_water) FROM facts WHERE area_water != "" ;'

area_land = pandas.read_sql_query(query, conn)
area_water = pandas.read_sql_query(query2, conn)
 
print(area_land['SUM(area_land)'][0] / area_water['SUM(area_water)'][0])