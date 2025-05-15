import mysql.connector
from csit314.config import DB_CONFIG

class CleanerListing:
    def __init__(self):
        self.conn = mysql.connector.connect(**DB_CONFIG)
        self.cursor = self.conn.cursor(dictionary=True)

    def get_by_user(self, user_id, query=None):
        self.conn.commit()  # Add this line to refresh from latest committed data        
        if query:
            sql = "SELECT * FROM service_listings WHERE user_id=%s AND service_name LIKE %s"
            self.cursor.execute(sql, (user_id, f"%{query}%",))
        else:
            sql = "SELECT * FROM service_listings WHERE user_id=%s"
            self.cursor.execute(sql, (user_id,))
        return self.cursor.fetchall()

    def get(self, service_id, user_id):
        self.conn.commit()  # Add this line to refresh from latest committed data  
        sql = "SELECT * FROM service_listings WHERE id=%s AND user_id=%s"
        self.cursor.execute(sql, (service_id, user_id))
        return self.cursor.fetchone()

    def add(self, user_id, name, price, type, description):
        sql = "INSERT INTO service_listings (user_id, service_name, price, type, description) VALUES (%s, %s, %s, %s, %s)"
        self.cursor.execute(sql, (user_id, name, price, type, description))
        self.conn.commit()

    def update(self, service_id, user_id, name, price, type, description):
        sql = "UPDATE service_listings SET service_name=%s, price=%s, type=%s, description=%s WHERE id=%s AND user_id=%s"
        self.cursor.execute(sql, (name, price, type, description, service_id, user_id))
        self.conn.commit()

    def delete(self, service_id, user_id):
        sql = "DELETE FROM service_listings WHERE id=%s AND user_id=%s"
        self.cursor.execute(sql, (service_id, user_id))
        self.conn.commit()

    def increment_shortlisted(self, service_id):
        self.cursor.execute("UPDATE service_listings SET shortlisted = shortlisted + 1 WHERE id = %s", (service_id,))
        self.conn.commit()              

    def get_service_listing_detail(self, service_id):
        # Increment total_views
        self.cursor.execute("UPDATE service_listings SET total_views = total_views + 1 WHERE id = %s", (service_id,))
        self.conn.commit()

        self.cursor.execute(
            """
            SELECT s.service_name, s.price, s.type, s.description,
                u.first_name, u.last_name, u.email, u.sex
            FROM service_listings s
            JOIN users u ON s.user_id = u.user_id
            WHERE s.id = %s
            """, (service_id,)
        )
        return self.cursor.fetchone()     
     
    def search_service_listings(self, name=None, email=None, service_name=None, min_price=None, max_price=None, type=None):
        self.conn.commit()  # Add this line to refresh from latest committed data  
        query = """
            SELECT s.id, s.service_name, s.price, s.type, s.description, s.total_views,
                   u.first_name, u.last_name, u.email
            FROM service_listings s
            JOIN users u ON s.user_id = u.user_id
            WHERE s.status = 'active'
        """
        filters = []
        values = []

        if name:
            query += " AND (c.first_name LIKE %s OR c.last_name LIKE %s)"
            filters.extend([f"%{name}%", f"%{name}%"])
        if email:
            query += " AND c.email LIKE %s"
            filters.append(f"%{email}%")
        if service_name:
            query += " AND s.service_name LIKE %s"
            filters.append(f"%{service_name}%")
        if type:
            query += " AND s.type = %s"
            filters.append(type)
        if min_price:
            query += " AND s.price >= %s"
            filters.append(min_price)
        if max_price:
            query += " AND s.price <= %s"
            filters.append(max_price)

        self.cursor.execute(query, filters)
        results = self.cursor.fetchall()

        return [{
            "id": row["id"],
            "service_name": row["service_name"],
            "price": row["price"],
            "type": row["type"],
            "description": row["description"],
            "total_views": row["total_views"],
            "first_name": row["first_name"],
            "last_name": row["last_name"],
            "email": row["email"]
        } for row in results]     