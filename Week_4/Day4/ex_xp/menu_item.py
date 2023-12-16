import psycopg2
import os
from dotenv import load_dotenv

# Load variables from the .env file into the environment
load_dotenv()


class MenuItem:
    def __init__(self, name, price, item_id=None):
        self.item_id = item_id
        self.name = name
        self.price = price

    def save(self):
        connection = psycopg2.connect(
            dbname=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            host=os.getenv('DB_HOST'),
            port=os.getenv('DB_PORT')
        )

        cursor = connection.cursor()

        cursor.execute(
            "INSERT INTO Menu_Items (item_name, item_price) VALUES (%s, %s) RETURNING item_id;",
            (self.name, self.price)
        )

        self.item_id = cursor.fetchone()[0]

        connection.commit()
        connection.close()

    def delete(self):
        if self.item_id is not None:
            connection = psycopg2.connect(
                dbname=os.getenv('DB_NAME'),
                user=os.getenv('DB_USER'),
                password=os.getenv('DB_PASSWORD'),
                host=os.getenv('DB_HOST'),
                port=os.getenv('DB_PORT')
            )

            cursor = connection.cursor()

            cursor.execute("DELETE FROM Menu_Items WHERE item_id = %s;", (self.item_id,))

            connection.commit()
            connection.close()

    def update(self, new_name=None, new_price=None):
        if self.item_id is not None:
            connection = psycopg2.connect(
                dbname=os.getenv('DB_NAME'),
                user=os.getenv('DB_USER'),
                password=os.getenv('DB_PASSWORD'),
                host=os.getenv('DB_HOST'),
                port=os.getenv('DB_PORT')
            )

            cursor = connection.cursor()

            update_query = "UPDATE Menu_Items SET"
            update_values = []

            if new_name is not None:
                update_query += " item_name = %s,"
                update_values.append(new_name)

            if new_price is not None:
                update_query += " item_price = %s,"
                update_values.append(new_price)

            update_query = update_query.rstrip(",")

            update_query += " WHERE item_id = %s;"
            update_values.append(self.item_id)

            cursor.execute(update_query, tuple(update_values))

            connection.commit()
            connection.close()