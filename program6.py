# Function to simulate connecting to a database
def connect_to_database(username, password):
    if username == "admin" and password == "ohnomypassword":
        return "Connected to the database!"
    else:
        return "Failed to connect to the database."

# Call the function
print(connect_to_database("admin", "your_db_password_here"))

# Secret: db_password
password = "ohnomypassword"
print(f"Database Password: {password}")
