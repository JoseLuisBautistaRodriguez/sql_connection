import MySQLdb

try:
    # Establish a connection to the MySQL server.
    # - 'host': The IP address of the server you discovered (e.g., the host running XAMPP).
    # - 'port': The TCP port for MySQL. If XAMPP is configured on port 3300, use 3300.
    # - 'user': The MySQL username with privileges to connect and query.
    # - 'passwd': The password for the specified user.
    db = MySQLdb.connect(
        host="172.19.0.0",     # IP you found, or localhost
        port=3306,             # For instance, "n" if XAMPP uses that port
        user="",
        passwd=""
    )

    print("Successfully connected to the database.")

    # Create a cursor object to execute queries.
    cursor = db.cursor()

    # Execute an SQL statement to show all available databases.
    cursor.execute("SHOW DATABASES;")

    # Fetch all the rows returned by the query.
    databases = cursor.fetchall()

    print("Available databases:")
    # Loop through each row (database name) returned
    for (db_name,) in databases:
        print(f"  - {db_name}")

# Catch any MySQLdb errors (e.g., connection issues, authentication problems, etc.).
except MySQLdb.Error as e:
    error_code, error_msg = e.args
    print(f"Error connecting: Code {error_code}, Message: {error_msg}")

