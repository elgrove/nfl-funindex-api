import sqlite3
from scraper import update_db

con = sqlite3.connect('backend/db.db')

cur = con.cursor()

update_db(cur)

con.commit()