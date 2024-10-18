from connect_mysql import connect_database

# Establishing the connection
conn = connect_database()
if conn is not None:
    try:
        cursor = conn.cursor()

        # Customer to be removed. Assuming John Doe has an id of 15
        customer_to_remove = (9, )

        query_check = "SELECT * FROM Orders WHERE customer_id = %s"
        cursor.execute(query_check, customer_to_remove)
        orders = cursor.fetchall()

        if orders:
            print("Cannot delete customer: Customer has associated orders.")
        else:
            # SQL query 
            query = "DELETE FROM Customers WHERE id = %s"

            # Executing the query
            cursor.execute(query, customer_to_remove)
        conn.commit()
        print("Customer removed successfully.")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        cursor.close()
        conn.close()