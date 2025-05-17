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
        self.cursor.execute(sql, (user_id,))
        return self.cursor.fetchone()

    def get_all_profiles(self):
        """Get all user profiles with user information"""
        self.conn.commit()
        
        query = """
            SELECT p.*, u.first_name, u.last_name, u.email, u.role, u.status
            FROM user_profiles p
            JOIN users u ON p.user_id = u.user_id
            ORDER BY u.role, u.first_name, u.last_name
        """
        
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def add(self, bio, avatar, status):
        """Create a new user profile"""
        sql = "INSERT INTO user_profiles (bio, avatar, status) VALUES (%s, %s, 'active')"
        self.cursor.execute(sql, (bio, avatar, status))
        self.conn.commit()
        return self.cursor.lastrowid
    
    def search_profiles(self, id=None, bio=None, first_name=None, last_name=None, email=None, role=None, status=None):
        """Search for user profiles"""

        self.conn.commit()
        query = """
            SELECT p.bio, u.user_id, u.first_name, u.last_name, u.email, u.role, u.status
            FROM users u
            JOIN profiles p ON u.user_id = p.user_id
            WHERE 1=1
        """
        params = []
        
        if id:
            query += " AND user_id = %s"
            params.append(id)
        if first_name:
            query += " AND first_name LIKE %s"
            params.append(f"%{first_name}%")
        if last_name:
            query += " AND last_name LIKE %s"
            params.append(f"%{last_name}%")
        if email:
            query += " AND email LIKE %s"
            params.append(f"%{email}%")
        if role:
            query += " AND role = %s"
            params.append(role)
        if bio: 
            query += " AND bio = %s"
            
        query += " ORDER BY role, id, first_name, last_name"
        
        self.cursor.execute(query, params)
        return self.cursor.fetchall()
    
    def update_profile(self, profile_id, role=None, description=None):
        """Update user profile"""
        updates = []
        params = []
        
        if bio is not None:
            updates.append("role = %s")
            params.append(role)
        
        if avatar is not None:
            updates.append("description = %s")
            params.append(description)
        
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
        self.cursor.execute("SELECT user_id FROM user_profiles WHERE profile_id=%s", (profile_id,))
        profile_result = self.cursor.fetchone()
        
        if not profile_result:
            return None  # Profile not found
        
        user_id = profile_result['user_id']
        
        # Now get the current user status
        check_sql = "SELECT status FROM users WHERE user_id = %s"
        self.cursor.execute(check_sql, (user_id,))
        result = self.cursor.fetchone()
        
        # Assuming user is always found
        if result.get('status') == 'active':
            # If status is 'active', set to 'inactive'
            update_sql = "UPDATE users SET status = 'inactive' WHERE user_id = %s"
            self.cursor.execute(update_sql, (user_id,))
            self.conn.commit()
            return True  # Was active, now inactive
        else:
            # If not active, set to 'active'
            update_sql = "UPDATE users SET status = 'active' WHERE user_id = %s"
            self.cursor.execute(update_sql, (user_id,))
            self.conn.commit()
            return False  # Was inactive, now active
