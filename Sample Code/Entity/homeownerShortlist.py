import mysql.connector
from csit314.config import DB_CONFIG

class HomeownerShortlist:
    def __init__(self):
        self.conn = mysql.connector.connect(**DB_CONFIG)
        self.cursor = self.conn.cursor(dictionary=True)

    def get_shortlisted_listings(self, user_id):
        """Get all shortlisted listings for a homeowner with details"""
        self.conn.commit()  # Refresh from latest committed data
        
        query = """
            SELECT s.id, s.service_name, s.price, s.type, s.description, s.total_views,
                   u.first_name, u.last_name, u.email, sl.create_date as shortlisted_date
            FROM shortlisted_listings sl
            JOIN service_listings s ON sl.listing_id = s.id
            JOIN users u ON s.user_id = u.user_id
            WHERE sl.user_id = %s
            ORDER BY sl.create_date DESC
        """
        
        self.cursor.execute(query, (user_id,))
        return self.cursor.fetchall()

    def is_shortlisted(self, user_id, listing_id):
        self.conn.commit()  # Add this line to refresh from latest committed data  
        self.cursor.execute(
            "SELECT * FROM shortlisted_listings WHERE user_id = %s AND listing_id = %s",
            (user_id, listing_id)
        )
        return self.cursor.fetchone() is not None

    def add_shortlist(self, user_id, listing_id):
        self.cursor.execute(
            "INSERT INTO shortlisted_listings (user_id, listing_id) VALUES (%s, %s)",
            (user_id, listing_id)
        )
        self.conn.commit()

    def remove_shortlist(self, user_id, listing_id):
        self.cursor.execute(
            "DELETE FROM shortlisted_listings WHERE user_id = %s AND listing_id = %s",
            (user_id, listing_id)
        )
        self.conn.commit()
      
