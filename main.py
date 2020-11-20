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


# Function for run SQL query
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


# Function for run Select Queries
def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


create_users_table = """
CREATE TABLE IF NOT EXISTS users (
  id INT AUTO_INCREMENT, 
  name TEXT NOT NULL, 
  age INT, 
  gender TEXT, 
  nationality TEXT, 
  PRIMARY KEY (id)
) ENGINE = InnoDB
"""

create_posts_table = """
CREATE TABLE IF NOT EXISTS posts (
  id INT AUTO_INCREMENT, 
  title TEXT NOT NULL, 
  description TEXT NOT NULL, 
  user_id INTEGER NOT NULL, 
  FOREIGN KEY fk_user_id (user_id) REFERENCES users(id), 
  PRIMARY KEY (id)
) ENGINE = InnoDB
"""

create_likes_table = """
CREATE TABLE IF NOT EXISTS likes (
  id INT AUTO_INCREMENT, 
  user_id INT NOT NULL, 
  post_id INT NOT NULL, 
  FOREIGN KEY fk_user_id (user_id) REFERENCES users(id),
  FOREIGN KEY fk_user_id(post_id) REFERENCES posts(id)
);
"""

create_users = """
INSERT INTO
  `users` (`name`, `age`, `gender`, `nationality`)
VALUES
  ('James', 25, 'male', 'USA'),
  ('Leila', 32, 'female', 'France'),
  ('Brigitte', 35, 'female', 'England'),
  ('Mike', 40, 'male', 'Denmark'),
  ('Elizabeth', 21, 'female', 'Canada');
"""

connection = create_connection("localhost", "root", "Splinter222", "sm_app")
select_users = "SELECT * FROM users"
users = execute_read_query(connection, select_users)
for user in users:
    print(user)



# execute_query(connection, create_likes_table)
# execute_query(connection, create_users_table)
# execute_query(connection, create_posts_table)
# create_database_query = "CREATE DATABASE sm_app"
# create_database(connection, create_database_query)
