import sqlite3

con = sqlite3.connect('backend/db.db')

cur = con.cursor()

from scraper import get_games, scrape_game

game_ = scrape_game('https://www.pro-football-reference.com/boxscores/202009200htx.htm')

create_table = '''create table raw (
    match_id text primary key,
    date text,
    time text,
    week integer,
    season integer,
    teama_name integer,
    teama_pts integer,
    teama_pts_q1 integer,
    teama_pts_q2 integer,
    teama_pts_q3 integer,
    teama_pts_q4 integer,
    teama_yds integer,
    teama_yds_rush integer,
    teama_yds_pass integer,
    teama_tds integer,
    teama_tds_rush integer,
    teama_tds_pass integer,
    teama_tos integer,
    teama_4d_att integer,
    teama_4d_comp integer,
    teama_sacks integer,
    teama_sack_yds integer,
    teama_rtn_td integer,
    teama_drives integer,
    teamh_name text,
    teamh_pts integer,
    teamh_pts_q1 integer,
    teamh_pts_q2 integer,
    teamh_pts_q3 integer,
    teamh_pts_q4 integer,
    teamh_yds integer,
    teamh_yds_rush integer,
    teamh_yds_pass integer,
    teamh_tds integer,
    teamh_tds_rush integer,
    teamh_tds_pass integer,
    teamh_tos integer,
    teamh_4d_att integer,
    teamh_4d_comp integer,
    teamh_sacks integer,
    teamh_sack_yds integer,
    teamh_rtn_td integer,
    teamh_drives integer)
'''


cur.execute(create_table)

