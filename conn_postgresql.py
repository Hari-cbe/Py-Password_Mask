# Pip install psycopg2 (If Not installed) 
import psycopg2
from password_utils import get_password


password = get_password()

# Connecting to postgres SQL Database
conn = psycopg2.connect(database="postgres",
                        user="postgres",
                        host='localhost',
                        password=password(),
                        port=5432)

print("DB Connected")
conn.close()