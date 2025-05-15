import mysql.connector
from csit314.config import DB_CONFIG

class HomeownerShortlist:
    def __init__(self):
        self.conn = mysql.connector.connect(**DB_CONFIG)
        self.cursor = self.conn.cursor(dictionary=True)

    def get_shortlisted_ids(self, user_id):
        self.conn.commit()  # Add this line to refresh from latest committed data  
        self.cursor.execute("SELECT listing_id FROM shortlisted_listings WHERE user_id = %s", (user_id,))
        return [row["listing_id"] for row in self.cursor.fetchall()]

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
      