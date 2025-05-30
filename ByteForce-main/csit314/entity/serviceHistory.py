import mysql.connector
from csit314.config import DB_CONFIG

class ServiceHistory:
    def __init__(self):
        self.conn = mysql.connector.connect(**DB_CONFIG)
        self.cursor = self.conn.cursor(dictionary=True)
    
    def get_cleaner_history(self, cleaner_id, service_type=None, start_date=None, end_date=None):
        """Get service history for a cleaner with optional filters"""
        self.conn.commit()  # Refresh from latest committed data
        
        query = """
            SELECT sh.id, sh.service_date, sh.service_type, sh.price, sh.status,
                   h.first_name as h_first_name, h.last_name as h_last_name, h.email as h_email,
                   c.first_name as c_first_name, c.last_name as c_last_name, c.email as c_email, 
                   sl.service_name, sl.description
            FROM service_history sh
            JOIN users h ON sh.homeowner_id = h.user_id
            JOIN users c ON sh.cleaner_id = c.user_id
            LEFT JOIN service_listings sl ON sh.service_listing_id = sl.id            
            WHERE sh.cleaner_id = %s
        """
        params = [cleaner_id]
        
        if service_type:
            query += " AND sh.service_type = %s"
            params.append(service_type)
        
        if start_date:
            query += " AND sh.service_date >= %s"
            params.append(start_date)
            
        if end_date:
            query += " AND sh.service_date <= %s"
            params.append(end_date)
            
        query += " ORDER BY sh.service_date DESC"
        
        self.cursor.execute(query, params)
        return self.cursor.fetchall()
        
    def get_homeowner_history(self, homeowner_id, service_type=None, start_date=None, end_date=None):
        """Get service history for a homeowner with optional filters"""
        self.conn.commit()  # Refresh from latest committed data
        
        query = """
            SELECT sh.id, sh.service_date, sh.service_type, sh.price, sh.status,
                   h.first_name as h_first_name, h.last_name as h_last_name, h.email as h_email,
                   c.first_name as c_first_name, c.last_name as c_last_name, c.email as c_email,
                   sl.service_name, sl.description
            FROM service_history sh
            JOIN users h ON sh.homeowner_id = h.user_id
            JOIN users c ON sh.cleaner_id = c.user_id
            LEFT JOIN service_listings sl ON sh.service_listing_id = sl.id
            WHERE sh.homeowner_id = %s
        """
        params = [homeowner_id]
        
        if service_type:
            query += " AND sh.service_type = %s"
            params.append(service_type)
        
        if start_date:
            query += " AND sh.service_date >= %s"
            params.append(start_date)
            
        if end_date:
            query += " AND sh.service_date <= %s"
            params.append(end_date)
            
        query += " ORDER BY sh.service_date DESC"
        
        self.cursor.execute(query, params)
        return self.cursor.fetchall()
    
    def get_history_detail(self, history_id):
        """Get detailed information about a specific service history entry"""
        self.conn.commit()
        
        query = """
            SELECT sh.*, 
                   c.first_name as cleaner_first_name, c.last_name as cleaner_last_name, c.email as cleaner_email,
                   h.first_name as homeowner_first_name, h.last_name as homeowner_last_name, h.email as homeowner_email,
                   sl.service_name, sl.description, sl.type
            FROM service_history sh
            JOIN users c ON sh.cleaner_id = c.user_id
            JOIN users h ON sh.homeowner_id = h.user_id
            LEFT JOIN service_listings sl ON sh.service_listing_id = sl.id
            WHERE sh.id = %s
        """
        
        self.cursor.execute(query, (history_id,))
        return self.cursor.fetchone()
