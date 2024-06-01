import mysql.connector
from mysql.connector import Error

def create_db_connection():
    try:
        connection = mysql.connector.connect(
            host='subway-testing-data.cbpery5zxigl.ap-south-1.rds.amazonaws.com',
            user='admin',
            password='XqSF8BfRIK0qzXmxxWr9',
            database='subway'
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        return None
