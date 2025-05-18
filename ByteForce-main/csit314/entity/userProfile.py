import mysql.connector
from csit314.config import DB_CONFIG

class UserProfile:
    def __init__(self):
        self.conn = mysql.connector.connect(**DB_CONFIG)
        self.cursor = self.conn.cursor(dictionary=True)
        
    def get_profile_by_user_id(self, user_id):
        """Get user profile by user ID"""
        self.conn.commit()
        sql = "SELECT * FROM user_profiles WHERE user_id=%s"
        self.cursor.execute(sql, (user_id))
        return self.cursor.fetchone()

    def get_all_profiles(self):
        """Get all user profiles with user information"""
        self.conn.commit()
        
        query = """
            SELECT p.id, p.status, u.first_name, u.last_name, u.email, u.role
            FROM user_profiles p
            JOIN users u ON p.user_id = u.user_id
            ORDER BY u.role, u.first_name, u.last_name
        """
        
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def add(self, user_id, bio, avatar):
        """Create a new user profile"""
        sql = "INSERT INTO user_ (user_id, bio, avatar) VALUES (%s, %s, %s)"
        self.cursor.execute(sql, (user_id, bio, avatar))
        self.conn.commit()
        return self.cursor.lastrowid
    
    def search_profiles(self, id=None, status=None, uid=None, role=None, first_name=None, last_name=None, email=None):
        """Search for user profiles"""
        self.conn.commit()
        query = """
            SELECT p.id, p.status, u.user_id, u.first_name, u.last_name, 
                   u.email, u.role
            FROM users u
            LEFT JOIN user_profiles p ON u.user_id = p.user_id
            WHERE 1=1
        """
        params = []
        
        if id:
            query += " AND p.id = %s"
            params.append(id)
        if uid: 
            query += " AND u.user_id = %s"
            params.append(uid)
        if status:
            query += " AND p.status = %s"
        if first_name:
            query += " AND u.first_name LIKE %s"
            params.append(f"%{first_name}%")
        if last_name:
            query += " AND u.last_name LIKE %s"
            params.append(f"%{last_name}%")
        if email:
            query += " AND u.email LIKE %s"
            params.append(f"%{email}%")
        if role:
            query += " AND u.role = %s"
            params.append(role)
        query += " ORDER BY u.role, u.first_name, u.last_name"
        
        self.cursor.execute(query, params)
        return self.cursor.fetchall()
    
    def update_profile(self, profile_id, bio=None, avatar=None):
        """Update user profile"""
        updates = []
        params = []
        
        if bio is not None:
            updates.append("bio = %s")
            params.append(bio)
        
        if avatar is not None:
            updates.append("avatar = %s")
            params.append(avatar)
        
        if not updates:
            return True  # Nothing to update
        
        query = f"UPDATE user_profiles SET {', '.join(updates)} WHERE profile_id = %s"
        params.append(profile_id)
        
        self.cursor.execute(query, params)
        self.conn.commit()
        return True
    
    def toggle_profile_status(self, profile_id):
        """Toggle profile status (requires finding associated user)"""
        # First get the user_id associated with this profile
        self.cursor.execute("SELECT id FROM user_profiles WHERE id=%s", (profile_id))
        profile_result = self.cursor.fetchone()
        
        if not profile_result:
            return None  # Profile not found
        
        user_id = profile_result['user_id']
        
        # Now get the current user status
        check_sql = "SELECT status FROM user_profiles WHERE user_id = %s"
        self.cursor.execute(check_sql, (user_id,))
        result = self.cursor.fetchone()
        
        # Assuming user is always found
        if result.get('status') == 'active':
            # If status is 'active', set to 'inactive'
            update_sql = "UPDATE user_profiles SET status = 'inactive' WHERE user_id = %s"
            self.cursor.execute(update_sql, (user_id,))
            self.conn.commit()
            return True  # Was active, now inactive
        else:
            # If not active, set to 'active'
             update_sql = "UPDATE user_profiles SET status = 'active' WHERE user_id = %s"
            self.cursor.execute(update_sql, (user_id,))
            self.conn.commit()
            return False 
            update_sql = "UPDATE users SET status = 'active' WHERE user_id = %s"
            self.cursor.execute(update_sql, (user_id,))
            self.conn.commit()
            return False  # Was inactive, now active
