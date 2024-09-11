import psycopg2

def fetch_cats_data():
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
        
        # Execute a query to fetch data from the 'cats' table
        cursor.execute("SELECT * FROM cats;")
        
        # Fetch all rows from the executed query
        cats_data = cursor.fetchall()
        
        # Print the fetched data
        for row in cats_data:
            print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Breed: {row[3]}")
    
    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)
    
    finally:
        # Close the database connection
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

if __name__ == "__main__":
    fetch_cats_data()