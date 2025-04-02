# Pip install psycopg2 (If Not installed) 
import psycopg2

# Connecting to postgres SQL Database
conn = psycopg2.connect(database = "postgres", 
                        user = "postgres", 
                        host= 'localhost',
                        password = "root",
                        port = 5432)


print("DB Connected")