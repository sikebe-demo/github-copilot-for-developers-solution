import psycopg2

def fetch_cats_data():
    try:
        # データベースに接続
        connection = psycopg2.connect(
            host="localhost",
            database="cats_db",
            user="admin",
            password="P@ssw0rd"
        )
        cursor = connection.cursor()

        # データを取得
        cursor.execute("SELECT * FROM cats;")
        rows = cursor.fetchall()

        # データを表示
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Breed: {row[3]}")

    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)
    finally:
        # 接続を閉じる
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

if __name__ == "__main__":
    fetch_cats_data()