import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

from menu_item import MenuItem  

class MenuManager:
    @classmethod
    def get_by_name(cls, item_name):
        connection = psycopg2.connect(
            dbname=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            host=os.getenv('DB_HOST'),
            port=os.getenv('DB_PORT')
        )

        cursor = connection.cursor()

        cursor.execute("SELECT * FROM Menu_Items WHERE item_name = %s;", (item_name,))

        result = cursor.fetchone()

        connection.close()

        if result is not None:
            item_id, name, price = result
            return MenuItem(name=name, price=price, item_id=item_id)
        else:
            return None


class MenuManager:
    @classmethod
    def all_items(cls):
        connection = psycopg2.connect(
            dbname=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            host=os.getenv('DB_HOST'),
            port=os.getenv('DB_PORT')
        )

        cursor = connection.cursor()

        cursor.execute("SELECT * FROM Menu_Items;")

        results = cursor.fetchall()

        connection.close()

        items = []
        for result in results:
            item_id, name, price = result
            item = MenuItem(name=name, price=price, item_id=item_id)
            items.append(item)

        return items





item = MenuItem('Burger', 35)
item.save()
item.delete()
item.update('Veggie Burger', 37)
item2 = MenuManager.get_by_name('Beef Stew')
items = MenuManager.all()

    
