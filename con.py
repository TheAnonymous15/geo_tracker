import pymysql

timeout = 10
connection = pymysql.connect(
    charset="utf8mb4",
    connect_timeout=timeout,
    cursorclass=pymysql.cursors.DictCursor,
    db="defaultdb",
    host="mysql-1835f891-muthikedaniel59-3cd3.f.aivencloud.com",
    password="AVNS_FuKonv4kaJf6_rez70_",
    read_timeout=timeout,
    port=27713,
    user="avnadmin",
    write_timeout=timeout,
)

try:
    with connection.cursor() as cursor:
        # Check if the table exists
        cursor.execute("SHOW TABLES LIKE 'AssetLocation'")
        table_exists = cursor.fetchone()

        if not table_exists:
            # Create the table if it does not exist
            cursor.execute("""
                CREATE TABLE AssetLocation (
                    Device_ID VARCHAR(200) NOT NULL,
                    location_latitude VARCHAR(200) NOT NULL,
                    location_longitude VARCHAR(200) NOT NULL,
                    location_name VARCHAR(200) NOT NULL,
                    PRIMARY KEY (Device_ID)
                ) ENGINE=MyISAM;
            """)
            print("AssetLocation table created successfully.")

        # You can now perform other operations with the connection
        # For example, inserting data into the table
        cursor.execute("INSERT INTO AssetLocation (Device_ID, location_latitude, location_longitude, location_name) VALUES ('device001', '40.7128', '-74.0060', 'New York')")
        connection.commit()

        # Fetch and print data from the table
        cursor.execute("SELECT * FROM AssetLocation")
        print(cursor.fetchall())

except Exception as e:
    print(f"Error: {e}")

finally:
    connection.close()
