import mysql.connector
from mysql.connector import Error


def create_connection(host_name, db_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            database=db_name,
            user=user_name,
            passwd=user_password
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection


connection = create_connection("mariadb.intexsoft.by", "expertise-keeper-qa", "expertise-keeper-qa", "pvhtYGL5mN")


def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


select_languages = "SELECT * FROM logs WHERE username = 'denis.metelitsa'"
languages = execute_read_query(connection, select_languages)


for language in languages:
    print(language)
