import mysql.connector
from csit314.config import DB_CONFIG

class UserAccount:
    def __init__(self):
        self.conn = mysql.connector.connect(**DB_CONFIG)
        self.cursor = self.conn.cursor(dictionary=True)

    def getUser(self, email, password, role):
        sql = "SELECT * FROM users WHERE email=%s AND password=%s AND role=%s "
        self.cursor.execute(sql, (email, password, role))
        return self.cursor.fetchone()

