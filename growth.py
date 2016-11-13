import sqlite3
import pandas
import math

conn = sqlite3.connect("factbook.db")
query = "SELECT * FROM facts;"
facts = pandas.read_sql_query(query, conn)
filtered_facts = facts.dropna(axis = 0)

def pop_calc(pop, pop_growth):
    n = pop*math.e**(pop_growth/100*35)
    return n


#print(filtered_facts['population_growth'])
print(pop_calc(filtered_facts['population'], filtered_facts['population_growth']))