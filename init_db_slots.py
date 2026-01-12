import mysql.connector
from config import Config

def get_db_connection():
    conn = mysql.connector.connect(
        host=Config.MYSQL_HOST,
        user=Config.MYSQL_USER,
        password=Config.MYSQL_PASSWORD,
        database=Config.MYSQL_DB
    )
    return conn

def init_slots():
    print("Initializing slots using raw SQL...")
    conn = get_db_connection()
    cursor = conn.cursor()

    # 1. Create slots table
    # Schema: id, station_id, slot_number, is_blocked
    create_table_query = """
    CREATE TABLE IF NOT EXISTS slots (
        id INT AUTO_INCREMENT PRIMARY KEY,
        station_id INT NOT NULL,
        slot_number INT NOT NULL,
        is_blocked TINYINT(1) DEFAULT 0,
        FOREIGN KEY (station_id) REFERENCES ev_station(id) ON DELETE CASCADE
    )
    """
    try:
        cursor.execute(create_table_query)
        print("Table 'slots' created or already exists.")
    except mysql.connector.Error as err:
        print(f"Error creating table: {err}")
        # Build might fail if ev_station id type mismatch or something. 
        # Making it simpler if FK fails (though ideally we want FK)
        print("Attempting to create generic table without strict FK constraint just in case...")
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS slots (
            id INT AUTO_INCREMENT PRIMARY KEY,
            station_id INT NOT NULL,
            slot_number INT NOT NULL,
            is_blocked TINYINT(1) DEFAULT 0
        )
        """)

    # 2. Get all stations
    cursor.execute("SELECT id, name FROM ev_station")
    stations = cursor.fetchall()
    print(f"Found {len(stations)} stations.")

    # 3. Initialize slots for each station
    for station in stations:
        sid = station[0]
        sname = station[1]
        
        # Check if slots exist
        cursor.execute("SELECT COUNT(*) FROM slots WHERE station_id = %s", (sid,))
        count = cursor.fetchone()[0]
        
        if count == 0:
            print(f"Adding 10 slots for station '{sname}' (ID: {sid})...")
            for i in range(1, 11):
                # (station_id, slot_number, is_blocked)
                sql = "INSERT INTO slots (station_id, slot_number, is_blocked) VALUES (%s, %s, 0)"
                cursor.execute(sql, (sid, i))
        else:
            print(f"Station '{sname}' already has {count} slots.")

    conn.commit()
    conn.close()
    print("Initialization complete.")

if __name__ == "__main__":
    init_slots()
