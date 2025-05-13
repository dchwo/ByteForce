import mysql.connector
from csit314.config import DB_CONFIG

class PlatformManagerEntity:
    def __init__(self):
        self.conn = mysql.connector.connect(**DB_CONFIG)
        self.cursor = self.conn.cursor(dictionary=True)
    
    # Authentication methods
    def get_manager(self, username, password):
        sql = "SELECT * FROM platform_managers WHERE username=%s AND password=%s AND status='active'"
        self.cursor.execute(sql, (username, password))
        return self.cursor.fetchone()
    
    # Category management methods
    def get_categories(self, query=None, status=None):
        if query and status:
            sql = "SELECT * FROM service_categories WHERE name LIKE %s AND status=%s ORDER BY name"
            self.cursor.execute(sql, (f"%{query}%", status))
        elif query:
            sql = "SELECT * FROM service_categories WHERE name LIKE %s AND status!='deleted' ORDER BY name"
            self.cursor.execute(sql, (f"%{query}%",))
        elif status:
            sql = "SELECT * FROM service_categories WHERE status=%s ORDER BY name"
            self.cursor.execute(sql, (status,))
        else:
            sql = "SELECT * FROM service_categories WHERE status!='deleted' ORDER BY name"
            self.cursor.execute(sql)
        return self.cursor.fetchall()
    
    def get_category(self, category_id):
        sql = "SELECT * FROM service_categories WHERE id=%s"
        self.cursor.execute(sql, (category_id,))
        return self.cursor.fetchone()
    
    def add_category(self, name, description, min_price, max_price):
        sql = "INSERT INTO service_categories (name, description, min_price, max_price) VALUES (%s, %s, %s, %s)"
        self.cursor.execute(sql, (name, description, min_price, max_price))
        self.conn.commit()
    
    def update_category(self, category_id, name, description, min_price, max_price):
        sql = "UPDATE service_categories SET name=%s, description=%s, min_price=%s, max_price=%s WHERE id=%s"
        self.cursor.execute(sql, (name, description, min_price, max_price, category_id))
        self.conn.commit()
    
    def delete_category(self, category_id):
        # Mark as deleted
        sql = "UPDATE service_categories SET status='deleted' WHERE id=%s"
        self.cursor.execute(sql, (category_id,))
        self.conn.commit()
    
    def suspend_category(self, category_id):
        sql = "UPDATE service_categories SET status='suspended' WHERE id=%s"
        self.cursor.execute(sql, (category_id,))
        self.conn.commit()
    
    def activate_category(self, category_id):
        sql = "UPDATE service_categories SET status='active' WHERE id=%s"
        self.cursor.execute(sql, (category_id,))
        self.conn.commit()