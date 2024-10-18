from connect_mysql import connect_database

conn = connect_database()
if conn is not None:
    try:
        cursor = conn.cursor()

        # Updated John Doe details assuming he has an id of 13
        updated_customer = ("9876543210", 13)

        # SQL query
        query = "UPDATE Customers SET phone = %s WHERE id = %s"

        # Executing the query
        cursor.execute(query, updated_customer)
        conn.commit()
        print("Customer details updated successfully.")

    finally:
        cursor.close()
        conn.close()