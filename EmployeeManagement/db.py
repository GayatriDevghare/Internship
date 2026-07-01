import mysql.connector

try:
    conn=mysql.connector.connect(
        host="localhost",
        user="root",
        password="301023",
        database='student_db'
    )
    
    cursor=conn.cursor()
    print("Database Connected successfully")

except Exception as e :
    print("Database Connection Error: ",e)