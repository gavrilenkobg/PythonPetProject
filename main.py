import mysql.connector
from mysql.connector import Error


# Function for connecting to database
def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection


# Function for creating database
def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


connection = create_connection("localhost", "root", "Splinter222", "sm_app")


# create_database_query = "CREATE DATABASE sm_app"
# create_database(connection, create_database_query)