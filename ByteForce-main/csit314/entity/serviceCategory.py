import mysql.connector
from csit314.config import DB_CONFIG

class ServiceCategory:
    def __init__(self):
        self.conn = mysql.connector.connect(**DB_CONFIG)
        self.cursor = self.conn.cursor(dictionary=True)
    
    def get_all_categories(self):
        """Get all service categories"""
        self.conn.commit()
        self.cursor.execute("SELECT * FROM service_categories ORDER BY name")
        return self.cursor.fetchall()

    def get_active_categories(self):
        """Get all active service categories"""
        self.conn.commit()
        self.cursor.execute("SELECT * FROM service_categories WHERE status = 'active' ORDER BY name")
        return self.cursor.fetchall()
    
    def get_category(self, category_id):
        """Get a specific service category by ID"""
        self.conn.commit()
        self.cursor.execute("SELECT * FROM service_categories WHERE id = %s", (category_id,))
        return self.cursor.fetchone()
    
    def create_category(self, name, description, min_price=None, max_price=None):
        """Create a new service category"""
        sql = """
            INSERT INTO service_categories 
            (name, description, min_price, max_price, status) 
            VALUES (%s, %s, %s, %s, 'active')
        """
        self.cursor.execute(sql, (name, description, min_price, max_price))
        self.conn.commit()
        return self.cursor.lastrowid
    
    def update_category(self, category_id, name, description, min_price=None, max_price=None):
        """Update an existing service category"""
        sql = """
            UPDATE service_categories 
            SET name = %s, description = %s, min_price = %s, max_price = %s
            WHERE id = %s
        """
        self.cursor.execute(sql, (name, description, min_price, max_price, category_id))
        self.conn.commit()
    
    def delete_category(self, category_id):
        """Delete a service category"""
        sql = "DELETE FROM service_categories WHERE id = %s"
        self.cursor.execute(sql, (category_id,))
        self.conn.commit()
    
    def suspend_category_status(self, category_id):
        """Toggle a service category between active and inactive states"""
        # Check current status
        check_sql = "SELECT status FROM service_categories WHERE id = %s"
        self.cursor.execute(check_sql, (category_id,))
        result = self.cursor.fetchone()
        
        # Assuming category is always found
        if result.get('status') == 'active':
            # If status is 'active', set to 'inactive'
            update_sql = "UPDATE service_categories SET status = 'inactive' WHERE id = %s"
            self.cursor.execute(update_sql, (category_id,))
            self.conn.commit()
            return True  # Was active, now inactive
        else:
            # If not active, set to 'active'
            update_sql = "UPDATE service_categories SET status = 'active' WHERE id = %s"
            self.cursor.execute(update_sql, (category_id,))
            self.conn.commit()
            return False  # Was inactive, now active
    
    def search_categories(self, query=None, status=None):
        """Search for service categories by name or description"""
        self.conn.commit()
        
        sql = "SELECT * FROM service_categories WHERE 1=1"
        params = []
        
        if query:
            sql += " AND (name LIKE %s OR description LIKE %s)"
            params.extend([f"%{query}%", f"%{query}%"])
        
        if status:
            sql += " AND status = %s"
            params.append(status)
            
        sql += " ORDER BY name"
        
        self.cursor.execute(sql, params)
        return self.cursor.fetchall()
