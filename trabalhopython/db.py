
import psycopg2

conn = psycopg2.connect(
    dbname="postgres",       
    user="postgres",         
    password="root",    
    host="localhost",
    port="5432"
)


cursor = conn.cursor()
conn.autocommit = True
cursor.execute("CREATE DATABASE CRUD")

cursor.close()
conn.close()


