import sqlite3
from datetime import datetime, timedelta, date

TODAY = datetime.now().date()
class SQLighter:

    def __init__(self, database):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()
        


    def create_table(self, name_table):
        self.cursor.execute(f'CREATE TABLE user_expenses (name text, price text)')
        print('Таблица')
    

    def insert_to(self, expenses_name, expenses_price, created_at=TODAY):
        self.cursor.executescript(f'''
                            UPDATE user_expenses 
                            SET price = price + {expenses_price}
                            WHERE name = "{expenses_name}" and created_at = {created_at};

                            INSERT INTO user_expenses (name, price, created_at)
                            SELECT "{expenses_name}", {expenses_price}, "{created_at}"
                            WHERE (SELECT Changes() = 0)
                            ''')
        self.connection.commit()


    def get_expenses(sql_obj, res):
        expenses = ''
        price = 0
        for item in res:
            if item[0] not in expenses:
                expenses += f'\nЗа {item[0]} :\n'
            expenses += f'{item[1]} - {item[2]} сум\n'
            price += item[2]
        expenses += f'\nВсего потрачено : {price} сум'
        return expenses


    def select_today(self):
        sql = self.cursor.execute(f' SELECT created_at, name, price FROM user_expenses WHERE created_at = "{TODAY}" ').fetchall()
        return self.get_expenses(sql) 

    def select_week(self):
        sql = self.cursor.execute(f' SELECT created_at, name, price FROM user_expenses WHERE created_at >= "{TODAY - timedelta(days=7)}" ').fetchall()
        return self.get_expenses(sql) 


    def select_month(self):
        sql = self.cursor.execute(f' SELECT created_at, name, price FROM user_expenses WHERE created_at >= "{TODAY - timedelta(days=30)}" ').fetchall()
        return self.get_expenses(sql) 


    def delete_from(self, recording):
        self.cursor.execute(f'DELETE FROM user_expenses WHERE name = "{recording}" ')
        self.connection.commit()
        print(f'Запись : {recording} удалена !')
