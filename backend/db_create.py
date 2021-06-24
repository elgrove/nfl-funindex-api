import sqlite3
from scraper import update_db_year

con = sqlite3.connect('backend/db.db')

cur = con.cursor()

create_table = '''create table raw (
    match_id text primary key
    , date text
    , time text
    , week integer
    , season integer
    , ot integer
    , teama_name integer
    , teama_pts integer
    , teama_pts_q1 integer
    , teama_pts_q2 integer
    , teama_pts_q3 integer
    , teama_pts_q4 integer
    , teama_yds integer
    , teama_yds_rush integer
    , teama_yds_pass integer
    , teama_tds integer
    , teama_tds_rush integer
    , teama_tds_pass integer
    , teama_tos integer
    , teama_4d_att integer
    , teama_4d_comp integer
    , teama_sacks integer
    , teama_sack_yds integer
    , teama_rtn_td integer
    , teama_drives integer
    , teamh_name text
    , teamh_pts integer
    , teamh_pts_q1 integer
    , teamh_pts_q2 integer
    , teamh_pts_q3 integer
    , teamh_pts_q4 integer
    , teamh_yds integer
    , teamh_yds_rush integer
    , teamh_yds_pass integer
    , teamh_tds integer
    , teamh_tds_rush integer
    , teamh_tds_pass integer
    , teamh_tos integer
    , teamh_4d_att integer
    , teamh_4d_comp integer
    , teamh_sacks integer
    , teamh_sack_yds integer
    , teamh_rtn_td integer
    , teamh_drives integer)
'''


cur.execute(create_table)
print('DB and table raw created')

years = range(2018, 2021, 1)

for year in years:
    update_db_year(year, cur)
    print(f'Finished scraping {year}')

print(f'Data update from {min(years)} to {max(years)} complete')


summary_view = '''create view summary_view as
select match_id
, date
, time
, week
, season
, teama_name
, teamh_name
, teama_pts+teamh_pts as pts
, teama_pts_q4+teamh_pts_q4 as ptsqf
, teama_yds+teamh_yds as yds
, teama_tds+teamh_tds as tds
, teama_tos+teamh_tos as tos
, (teama_4d_comp+teamh_4d_comp)/(teama_4d_att+teamh_4d_att) as fdpc
, teama_sacks+teamh_sacks as sacks
, teama_sack_yds+teamh_sack_yds as sackyds
, (teama_rtn_td+teamh_rtn_td) as rtns
, teama_drives+teamh_drives as drives
, (teama_tds+teamh_tds)/(teama_drives+teamh_drives) as drvtdpc -- NOT WORKING
, case when teama_pts-teamh_pts <= 7 then 1 else 0 end as close
, case when (teama_pts-teama_pts_q4)-(teamh_pts-teamh_pts_q4) <= 7 then 1 else 0 end as closeqf
, ot
from raw;'''

cur.execute(summary_view)

print('Summary view created')

web_view = '''create view web_view as
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

cur.execute(web_view)

print('Web view created')

con.commit()

print('Committed')
