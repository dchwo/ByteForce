import mysql.connector
from datetime import datetime, timedelta
import random

# Service types and statuses
service_types = [
    "General Cleaning", "Deep Cleaning", "Carpet Cleaning",
    "Office Cleaning", "Janitorial Service", "Pressure Washing"
]
status_options = ['completed', 'cancelled', 'pending']

# Connect to the database
conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="password1",
    database="csit314"
)

cursor = conn.cursor()

# Fetch cleaner and homeowner user IDs from users table
cursor.execute("SELECT user_id FROM users WHERE role = 'cleaner' AND status = 'active'")
cleaner_ids = [row[0] for row in cursor.fetchall()]

cursor.execute("SELECT user_id FROM users WHERE role = 'homeowner' AND status = 'active'")
homeowner_ids = [row[0] for row in cursor.fetchall()]

# Fetch existing service_listing_ids
cursor.execute("SELECT id FROM service_listings")
service_listing_ids = [row[0] for row in cursor.fetchall()]

if not cleaner_ids or not homeowner_ids or not service_listing_ids:
    print("Missing required users or service listings. Aborting.")
else:
    for i in range(10):
        cleaner_id = random.choice(cleaner_ids)
        homeowner_id = random.choice(homeowner_ids)
        service_listing_id = random.choice(service_listing_ids)
        service_type = random.choice(service_types)
        service_date = (datetime.now() - timedelta(days=random.randint(1, 90))).date()
        price = round(random.uniform(100, 1000), 2)
        status = random.choice(status_options)
        notes = f"Auto-generated note {i+1}"
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        query = """
            INSERT INTO service_history (
                cleaner_id, homeowner_id, service_listing_id,
                service_type, service_date, price, status, notes,
                create_date, update_date
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        data = (
            cleaner_id, homeowner_id, service_listing_id,
            service_type, service_date, price, status, notes,
            timestamp, timestamp
        )
        cursor.execute(query, data)
        print(f"Inserted service history for cleaner_id={cleaner_id} : homeowner_id={homeowner_id} : '{service_type}'")

    conn.commit()
    print("✅ 10 service_history records inserted successfully.")

cursor.close()
conn.close()
