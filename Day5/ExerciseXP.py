
import psycopg2
import os
HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = os.environ['POSTGRESPASSWORD']
DATABASE = 'RestaurantMenu'


connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE )
cursor = connection.cursor()
query = "CREATE TABLE IF NOT EXISTS items( menu_item VARCHAR(1000) NOT NULL,item_price INTEGER NOT NULL)"
cursor.execute(query)
connection.commit()
connection.close()

class MenuItem():
    def __init__(self,name,price):
        self.name=name.strip()
        self.price=price
    def save(self):
        connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE )
        cursor = connection.cursor()
        query = f"INSERT INTO items(menu_item,item_price) VALUES('{self.name}',{self.price}) RETURNING *;"
        cursor.execute(query)
        results = cursor.fetchall()
        print(results)
        connection.commit()
        
        connection.close()
        return True
    
  
    def delete(self):
        connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE )
        cursor = connection.cursor()
        query = f"DELETE FROM items WHERE menu_item='{self.name}' AND item_price={self.price};"
        cursor.execute(query)
        # results = cursor.fetchall()
        connection.commit()
        connection.close()
        return True
    def update(self):
        connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE )
        cursor = connection.cursor()
        query = f"UPDATE items SET  menu_item='{self.name}', item_price={self.price};"
        cursor.execute(query)
        # results = cursor.fetchall()
        connection.commit()
        connection.close()
    @staticmethod 
    def all(self):
        MenuItem=[]
        return MenuItem
    @staticmethod
    def get_by_name(name):
        name=name.strip()
        connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE )
        cursor = connection.cursor()
        query = f"SELECT menu_item,item_price FROM items WHERE menu_item='{name}' ;"
        cursor.execute(query)
        print(query)
        results = cursor.fetchall()
        print(results)
        connection.commit()
        connection.close()
        try: 
            result = results[0]
            return MenuItem(result[0],result[1])
            
        except:
            print("This menu item does not exist ")
            return None
        
      

# menu=MenuItem(" chips",90)
# menu.get_by_name(" chips")
