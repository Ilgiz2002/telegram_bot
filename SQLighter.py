import sqlite3
from datetime import datetime, timedelta, date

TODAY = date(2020, 8, 16)
class SQLighter:

    def __init__(self, database):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()
        


    def create_table(self, name_table):
        self.cursor.execute(f'CREATE TABLE user_expenses (name text, price text)')
        print('Таблица')
    

    def insert_to(self, user_name, user_price, created_at=TODAY):
        self.cursor.executescript(f'''
                            UPDATE user_expenses 
                            SET price = price + {user_price}
                            WHERE name = "{user_name}" and created_at = {created_at};

                            INSERT INTO user_expenses (name, price, created_at)
                            SELECT "{user_name}", {user_price}, "{created_at}"
                            WHERE (SELECT Changes() = 0)
                            ''')
        self.connection.commit()

    def select_today(self):
        sql = self.cursor.execute(f' SELECT created_at, name, price FROM user_expenses WHERE created_at = "{TODAY}" ').fetchall()
        return sql

    def select_week(self):
        sql = self.cursor.execute(f' SELECT created_at, name, price FROM user_expenses WHERE created_at >= "{TODAY - timedelta(days=7)}" ').fetchall()
        return sql


    def select_month(self):
        sql = self.cursor.execute(f' SELECT created_at, name, price FROM user_expenses WHERE created_at >= "{TODAY - timedelta(days=30)}" ').fetchall()
        return sql


    def delete_from(self, recording):
        self.cursor.execute(f'DELETE FROM user_expenses WHERE name = "{recording}" ')
        self.connection.commit()
        print(f'Запись : {recording} удалена !')