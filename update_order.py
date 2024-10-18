from connect_mysql import connect_database

# Establishing the connection
conn = connect_database()
if conn is not None:
    try: 
        cursor = conn.cursor()

        # Details for the order update
        # Assuming we have John Does customer ID
        customer_id = 6
        # Assuming we have the order's ID and the new date
        order_id = 9 # Example order ID to te updated
        new_order_date = "2024-02-20"

        # SQL query
        query = "UPDATE Orders SET date = %s WHERE id = %s AND customer_id = %s"

        # Executing the query
        cursor.execute(query, (new_order_date, order_id, customer_id))
        conn.commit()
        print("Order updated successfully.")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        cursor.close()
        conn.close()
        