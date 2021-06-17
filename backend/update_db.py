import sqlite3
from scraper import update_db

con = sqlite3.connect('backend/db.db')

cursor = con.cursor()