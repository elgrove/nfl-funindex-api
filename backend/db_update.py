import sqlite3
from scraper import update_db
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

con = sqlite3.connect("db.db")

cur = con.cursor()

update_db(cur)

con.commit()
