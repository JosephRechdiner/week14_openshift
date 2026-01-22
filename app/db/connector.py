import mysql.connector
import os

config = {
    "host": os.getenv("MYSQL_HOST"),
    "user": os.getenv("MYSQL_USER"),
    "password": os.getenv("MYSQL_PASSWORD"),
    "database": os.getenv("MYSQL_DATABASE"),
}

class SQLManager:
    cnx = None
    def __init__(self):
        if not SQLManager.cnx:
            try:
                cnx = mysql.connector.connect(**config)
                SQLManager.cnx = cnx
            except Exception as e:
                raise Exception(f"Could not connect to db {str(e)}")
        self.cnx = SQLManager.cnx

    def get_cnx(self):
        return self.cnx
    
    def init_db(self):
        cnx = self.get_cnx()
        cursor = cnx.cursor()

        try:
            with open ("init.sql", "r") as file:
                statements = file.read().split(";")

            for statement in statements:
                statement = statement.strip()
                if statement:
                    cursor.execute(statement)
            cnx.commit()

        except Exception as e:
            raise Exception(f"Could not init db {str(e)}")