import sqlite3
from scraper import update_db_year

con = sqlite3.connect('backend/db.db')

cursor = con.cursor()

query = '''create view web_view as
select match_id
, date
, time
, week
, season
, teama_name
, teamh_name
, 
(
(pts * 0.04) + 
case when closeqf = 1 then ptsqf * 0.04 else ptsqf * 0.02 end + 
(yds*0.0008) + 
(tds * 0.15) + 
(tos * 0.08) + 
(close * 0.1) + 
(closeqf * 0.2) +
(sacks * 0.015) + 
(sackyds * 0.011) + 
(rtns * 0.3) + 
(ot * 0.15)
) as fun_score from summary_view;'''

cursor.execute(query)

con.commit()
