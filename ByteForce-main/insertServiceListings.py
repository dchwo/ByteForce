import mysql.connector
from datetime import datetime
import random

# Sample data pools
service_titles = [
    "Room Cleaning", "Flat Cleanup", "Office Maintenance",
    "Carpet Wash", "Post-Reno Cleaning", "Panel Polishing",
    "Dusting", "Deep Clean", "Patio Cleaning", "Garden Cleaning"
]

types = [
    "General Cleaning", "Deep Cleaning", "Carpet Cleaning",
    "Office Cleaning", "Janitorial Service", "Pressure Washing"
]

descriptions = [
    "Weekly cleaning session", "Full interior deep clean", "Carpet shampoo and vacuum",
    "Desk and meeting room cleaning", "Bathroom and kitchen scrubbing",
    "High-pressure water cleaning", "Heavy-duty dust removal", "Glass and facade polish",
    "Outdoor cleaning service", "Garden sweeping and maintenance"
]

# Connect to DB
conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="password1",
    database="csit314"
)

cursor = conn.cursor()

# Get all active cleaner user_ids
cursor.execute("SELECT user_id FROM users WHERE role = 'cleaner' AND status = 'active'")
cleaner_ids = [row[0] for row in cursor.fetchall()]

# Get all active category_ids
cursor.execute("SELECT id FROM service_categories WHERE status = 'active'")
category_ids = [row[0] for row in cursor.fetchall()]

if not cleaner_ids or not category_ids:
    print("Missing cleaner users or service categories.")
else:
    for cleaner_id in cleaner_ids:
        for i in range(10):  # Insert 10 listings per cleaner
            base_name = random.choice(service_titles)
            service_name = f"{base_name} ({random.randint(1, 100)})"
            type_value = random.choice(types)
            description = random.choice(descriptions)
            price = round(random.uniform(100, 800), 2)
            total_views = random.randint(0, 100)
            shortlisted = random.randint(0, 20)
            status = 'active'
            category_id = random.choice(category_ids)
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            query = """
                INSERT INTO service_listings (
                    user_id, service_name, type, description, price,
                    total_views, shortlisted, status, create_date, update_date, category_id
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            data = (
                cleaner_id, service_name, type_value, description, price,
                total_views, shortlisted, status, timestamp, timestamp, category_id
            )
            cursor.execute(query, data)
            print(f"Inserted service for cleaner_id={cleaner_id}: '{service_name}'")

    conn.commit()
    print(f"✅ Inserted {len(cleaner_ids) * 5} service_listings (5 per cleaner).")

cursor.close()
conn.close()
