import sqlite3
from Warrior import Warrior
from Hero import Hero
from Army import Army
from Option import Option
from ForeignOption import ForeignOption

class Database:
    def __init__(self, db):
        self.db = db
     
    def connect(self):
        return sqlite3.connect(self.db)

    def get_warrior(self, w):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Warriors WHERE Name LIKE ?', (w,))
        return Warrior.from_database(cursor.fetchone())

    def get_hero(self, h):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Heroes WHERE Name LIKE ?', (h,))
        return Hero.from_database(cursor.fetchone())

    def get_all_Warriors(self):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Warriors')
        return [Warrior.from_database(data) for data in cursor.fetchall()]

    def get_all_warriors_from_army(self, army):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Warriors WHERE isInArmy LIKE ?', (army,))
        return [Warrior.from_database(data) for data in cursor.fetchall()]

    def get_all_heroes_from_army(self, army):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Heroes WHERE isInArmy LIKE ?', (army,))
        return [Hero.from_database(data) for data in cursor.fetchall()]

    def get_all_armies(self):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Armies')
        return [Army.from_database(data) for data in cursor.fetchall()]

    def get_all_options_for_unit(self, name):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Options WHERE Unit LIKE ?', (name,))
        return [Option.from_database(data) for data in cursor.fetchall()]

    def get_all_foreign_options_for_unit(self, name):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM ForeignOptions WHERE ReceivingUnit LIKE ?', (name,))
        return [ForeignOption.from_database(data) for data in cursor.fetchall()]
