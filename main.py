import sqlite3
import os

units_data = [
    ("Espadachines", 60, 20, 0, 70),
    ("Arqueros", 80, 10, 40, 95),
    ("Jinetes", 140, 0, 100, 230)
]

def create_resources_db():
    conn = sqlite3.connect('recursos.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS resources (
            unit TEXT PRIMARY KEY,
            food INTEGER,
            wood INTEGER,
            gold INTEGER
        )
    ''')
    
    for unidad, comida, madera, oro, _ in units_data:
        cursor.execute('''
            INSERT OR REPLACE INTO resources (unit, food, wood, gold)
            VALUES (?, ?, ?, ?)
        ''', (unidad, comida, madera, oro))
    
    conn.commit()
    conn.close()

def create_soldiers_db():
    conn = sqlite3.connect('soldados.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS soldiers (
            unit TEXT PRIMARY KEY,
            power INTEGER
        )
    ''')
    
    for unidad, _, _, _, poder in units_data:
        cursor.execute('''
            INSERT OR REPLACE INTO soldiers (unit, power)
            VALUES (?, ?)
        ''', (unidad, poder))
    
    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_resources_db()
    create_soldiers_db()
    os.system('python poder.py')