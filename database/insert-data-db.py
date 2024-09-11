import psycopg2

def insert_cat_data(name, age, breed):
    try:
        # Connect to the PostgreSQL database
        connection = psycopg2.connect(
            dbname="cats_db",
            user="admin",
            password="P@ssw0rd",
            host="localhost",
            port="5432"
        )
        
        cursor = connection.cursor()
        
        # Execute a query to insert data into the 'cats' table
        insert_query = """INSERT INTO cats (name, age, breed) VALUES (%s, %s, %s);"""
        cursor.execute(insert_query, (name, age, breed))
        
        # Commit the transaction
        connection.commit()
        
        print("Data inserted successfully")
    
    except (Exception, psycopg2.Error) as error:
        print("Error while inserting data into PostgreSQL", error)
    
    finally:
        # Close the database connection
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

if __name__ == "__main__":
    # Example data to insert
    insert_cat_data('Tom', 4, 'Tabby')
    insert_cat_data('Jerry', 2, 'Siamese')