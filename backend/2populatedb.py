import sqlite3
from scraper import update_db_year

con = sqlite3.connect('backend/db.db')

cursor = con.cursor()

years = range(2018, 2020, 1)


for year in years:
    update_db_year(year, cursor)
    print(f'Finished scraping {year}')

# update_db_year(2020, cursor)

con.commit()
print('Data update committed')