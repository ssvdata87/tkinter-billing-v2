import sqlite3
import datetime

class Database:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()

        sql='''CREATE TABLE IF NOT EXISTS product(
            product_code INTEGER PRIMARY KEY autoincrement,
            product_name TEXT,
            product_price decimal(10,2)
        );'''

        sql1='''CREATE TABLE IF NOT EXISTS orders (
        order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_date DATE,
    TOTAL decimal(10,2)
    );'''
        
        sql2='''CREATE TABLE IF NOT EXISTS order_details(
        order_id INTEGER,
        product_code INTEGER,
        product_name TEXT,
        quantity INTEGER,
        product_price decimal(10,2),
        total decimal(10,2)
        );'''

        self.cursor.execute(sql)
        self.cursor.execute(sql1)   
        self.cursor.execute(sql2)
        self.conn.commit()

    def add_product(self, product_name, product_price):
        sql = '''INSERT INTO product(product_name, product_price) VALUES(?,?)'''
        self.cursor.execute(sql, (product_name, product_price))
        self.conn.commit()

    def show_product(self):
        sql = '''SELECT * FROM product'''
        self.cursor.execute(sql)
        return self.cursor.fetchall()
    
    def get_product(self, product_id):
        sql = '''SELECT * FROM product WHERE product_code=?'''
        self.cursor.execute(sql, (product_id,))
        return self.cursor.fetchone()
    
    def add_order_details(self, product_code,product_name,quantity,product_price,total):
        oder_id=0
        sql='''INSERT INTO order_details(order_id,product_code,product_name,quantity,product_price,total) VALUES(?,?,?,?,?,?)'''
        self.cursor.execute(sql,(oder_id,product_code,product_name,quantity,product_price,total))
        self.conn.commit()

   
    
    def get_order_details(self):
        sql='''SELECT product_name,quantity,product_price,total  FROM order_details where order_id=0'''
        self.cursor.execute(sql)
        return self.cursor.fetchall()
    
    def get_all_order_total(self):
        sql='''SELECT sum(total) FROM  order_details where order_id=0'''
        self.cursor.execute(sql)
        return self.cursor.fetchone()
   
    def save_order(self):
        order_date=datetime.date.today()
        all_total=self.get_all_order_total()
        sql='''INSERT INTO orders(order_date,TOTAL) VALUES(?,?)'''
        self.cursor.execute(sql, (order_date, all_total[0]))
        self.conn.commit()
        self.last_inserted_id=self.cursor.lastrowid    
        self.cursor.execute('UPDATE order_details SET order_id=? WHERE order_id=0',(self.last_inserted_id,))
        self.conn.commit()
    

