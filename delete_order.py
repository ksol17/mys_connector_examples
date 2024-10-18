from connect_mysql import connect_database

# Establishing the connection
conn = connect_database()
if conn is not None:
    try:
        cursor = conn.cursor()

        # Details for the order update
        # Assuming we have John Doe's customer ID
        customer_id = 6
        # Order ID to be deleted
        order_id = 9  

        # SQL query
        query = "DELETE FROM Orders WHERE id = %s AND customer_id = %s"

        # Executing the query
        cursor.execute(query, (order_id, customer_id))
        conn.commit()
        print("Order deleted successfully.")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        cursor.close()
        conn.close()