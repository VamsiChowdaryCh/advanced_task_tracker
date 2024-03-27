import mysql.connector

# Establish connection
mydb = mysql.connector.connect(
    host="35.170.246.36",
    user="test",
    password="Test@123",
    database="task_tracker"
)

# Create cursor
cursor = mydb.cursor()

# Execute query
cursor.execute("SELECT * FROM Categories")

# Fetch results
result = cursor.fetchall()
for row in result:
    print(row)

# Close connection
mydb.close()
