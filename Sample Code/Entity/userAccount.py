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
    
    def addUser(self, first_name, last_name, email, role, password, sex, birth_date):
        
        # Check if the email already exists
        checkQuery = "SELECT email FROM users u WHERE email = %s"
        self.cursor.execute(checkQuery, (email, role))
        existingUser = self.cursor.fetchone()

        if existingUser:
            self.cursor.close()
            return False  # User already exists

        else:
             # Check if the role status is 'active'
            roleStatusQuery = "SELECT status FROM profiles WHERE role = %s"
            self.cursor.execute(roleStatusQuery, (role,))
            roleStatus = self.cursor.fetchone()
            if not roleStatus or roleStatus.get('status') != 'active':
                self.cursor.close()
                return False  # Role is not active

            sql = """   
            INSERT INTO users
            (first_name, last_name, email, role, password, sex, birth_date) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """

            self.cursor.execute(sql, (
                first_name,
                last_name,
                email,
                role,
                password,
                sex,
                birth_date
            ))

            self.conn.commit()
            self.cursor.close()

            return True
    
    def getUserDetails(self, id):
        # Get the user details from the database
        sql = "SELECT * FROM users WHERE id = %s"
        self.cursor.execute(sql, (id,))
        return self.cursor.fetchone() 
    
    def updateUser(self, id, role, first_name, last_name, email, password):
        # Update the user details in the database
        updateQuery = """
        UPDATE users
        SET role = %s, first_name = %s, last_name = %s, email = %s, password = %s
        WHERE id = %s
        """
        self.cursor.execute(updateQuery, (role, first_name, last_name, email, password, id))
        self.conn.commit()
        self.cursor.close()
        return True   

    def suspendUser(self, id):
        # Check current status
        check_sql = "SELECT status FROM users WHERE id = %s"
        self.cursor.execute(check_sql, (id))
        result = self.cursor.fetchone()

        #Assuming user is always found
        if result.get('status') == 'active':
            # If status is 'active', set to 'inactive'
            update_sql = "UPDATE users SET status = 'inactive' WHERE id = %s"
            self.cursor.execute(update_sql, (id))
            self.conn.commit()
            return True
        
        else:
            # If not active, set to 'active'
            update_sql = "UPDATE users SET status = 'active' WHERE id = %s"
            self.cursor.execute(update_sql, (id,))
            self.conn.commit()
            return False 
    
    def searchUser(self, id=None, first_name=None, last_name=None, email=None, role=None):
        self.conn.commit()
        query = """
            SELECT id, first_name, last_name, email, role
            FROM users 
            WHERE 1=1
        """
        filters = []
        values = []
        if id:
            query += " AND id = %s"
            filters.append("id")
        if first_name:
            query += " AND first_name LIKE %s"
            filters.append(f"%{first_name}%")
        if last_name:
            query += " AND last_name LIKE %s"
            filters.append(f"%{last_name}%")
        if email:
            query += " AND email LIKE %s"
            filters.append(f"%{email}%")
        if role:
            query += " AND role LIKE %s"
            filters.append(f"%{role}%")

        self.cursor.execute(query, filters)
        results = self.cursor.fetchall()

        return [{
            "id": row["id"],
            "first_name": row["first_name"],
            "last_name": row["last_name"],
            "email": row["email"],
            "role": row["role"]
        } for row in results]
