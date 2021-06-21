import sqlite3
from scraper import update_db_year

con = sqlite3.connect('backend/db.db')

cursor = con.cursor()

query = '''create view summary_view as
select match_id
, date
, time
, week
, season
, teama_name
, teamh_name
, teama_pts+teamh_pts as pts
, teama_pts_q4+teamh_pts+q4 as ptsqf
, teama_yds+teamh_yds as yds
, teama_tds+teamh_tds as tds
, teama_tos+teamh_tos as tos
, (teama_4d_comp+teamh_4d_comp)/(teama_4d_att+teamh_4d_att) as fdpc
, teama_sacks+teamh_sacks as sacks
, teama_sack_yds+teamh_sack_yds as sackyds
, (teama_rtn_td+teamh_rtn_td) as rtns
, teama_drives+teamh_drives as drives
, (teama_tds+teamh_tds)/(teama_drives+teamh_drives) as drvtdpc
, case when teama_pts-teamh_pts <= 7 then 1 else 0 end as close
, case when (teama_pts-teama_pts_q4)-(teamh_pts-teamh_pts_q4) <= 7 then 1 else 0 end as closeqf
from raw;'''

cursor.execute(query)

con.commit()
