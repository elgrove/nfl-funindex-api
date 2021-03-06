import re
import requests
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import datetime as dt
import sqlite3
import math


def scrape_game(game):
    """scrapes game url returning a dict"""
    url = game
    res = requests.get(url)
    # use re to escape html comments
    comm = re.compile("<!--|-->")
    soup = BeautifulSoup(comm.sub("", res.text), "lxml")
    # get content div, holds all body content
    divs = soup.findAll("div", id="content")
    # table for points by quarter
    points = pd.read_html(res.text)[0]
    # table for scoring stats
    stats = pd.read_html(
        str(
            divs[0]
            .findAll("div", id=re.compile("^all_team_stats"))[0]
            .findAll("table")[0]
        )
    )[0]
    # length of drives table = number of drives
    home_drives = len(
        pd.read_html(str(divs[0].findAll("table", id="home_drives")))[0].index
    )
    away_drives = len(
        pd.read_html(str(divs[0].findAll("table", id="vis_drives")))[0].index
    )
    # kick and punt returns
    returns = pd.read_html(str(divs[0].findAll("table", id="returns")))[0]

    # get datetime object for the dict
    date_ = (
        divs[0]
        .findAll("div", class_="scorebox")[0]
        .findAll("div", class_="scorebox_meta")[0]
        .findAll("div")[0]
        .text
    )
    time_ = (
        divs[0]
        .findAll("div", class_="scorebox")[0]
        .findAll("div", class_="scorebox_meta")[0]
        .findAll("div")[1]
        .text.replace("Start Time: ", "")
    )
    datestr = date_ + " " + time_
    dateobj = dt.datetime.strptime(datestr, "%A %b %d, %Y %I:%M%p")

    # get week number, all of the playoffs is called week 18
    if soup.findAll("h2")[0].text.endswith("Playoffs") == True:
        week_ = "18"
    else:
        week_ = soup.findAll("h2")[0].text.replace("NFL Scores — Week ", "")

    if dateobj.month >= 7:
        season_ = dateobj.year
    else:
        season_ = dateobj.year - 1

    # kick/punt returns work
    split_row = None
    try:
        math.isnan(returns.iloc[0, 0])
        split_row = 0
    except:
        pass
    try:
        math.isnan(returns.iloc[1, 0])
        split_row = 1
    except:
        pass
    try:
        math.isnan(returns.iloc[2, 0])
        split_row = 2
    except:
        pass
    try:
        math.isnan(returns.iloc[3, 0])
        split_row = 3
    except:
        pass
    try:
        math.isnan(returns.iloc[4, 0])
        split_row = 4
    except:
        pass

    if split_row is not None:
        returns.columns = returns.columns.droplevel()
        away_returns = returns.copy().loc[: split_row - 1]
        away_returns.columns = [
            "Player",
            "Tm",
            "Rt",
            "Yds",
            "Y/Rt",
            "TD-kick",
            "Lng",
            "Ret",
            "Yds",
            "Y/R",
            "TD-punt",
            "Lng",
        ]
        home_returns = returns.copy().loc[split_row + 2 :]
        home_returns.columns = [
            "Player",
            "Tm",
            "Rt",
            "Yds",
            "Y/Rt",
            "TD-kick",
            "Lng",
            "Ret",
            "Yds",
            "Y/R",
            "TD-punt",
            "Lng",
        ]
        away_rtn_td = (
            away_returns["TD-kick"].astype(int).sum()
            + away_returns["TD-punt"].astype(int).sum()
        )
        home_rtn_td = (
            home_returns["TD-kick"].astype(int).sum()
            + home_returns["TD-punt"].astype(int).sum()
        )
    # ** imperfect hack alert **
    else:
        away_rtn_td = 0
        home_rtn_td = 0

    ot = 0
    if points.shape == (2, 8):
        ot = 1

    game_dict = {}

    game_dict.update(
        {
            "match_id": url[49:61],  # NOT INT
            "date": dateobj.date().strftime("%Y-%m-%d"),  # NOT INT
            "time": dateobj.time().strftime("%H:%M:%S"),  # NOT INT
            "week": int(week_),
            "season": int(season_),
            "ot": ot,
            "teama_name": points.iloc[0, 1],  # NOT INT
            "teama_pts": int(points.iloc[0, -1]),
            "teama_pts_q1": int(points.iloc[0, 2]),
            "teama_pts_q2": int(points.iloc[0, 3]),
            "teama_pts_q3": int(points.iloc[0, 4]),
            "teama_pts_q4": int(points.iloc[0, 5]),
            "teama_yds": int(stats.iloc[5, 1]),
            "teama_yds_rush": int(stats.iloc[1, 1].split("-")[1]),
            "teama_yds_pass": int(stats.iloc[2, 1].split("-")[2]),
            "teama_tds": int(stats.iloc[1, 1].split("-")[2])
            + int(stats.iloc[2, 1].split("-")[3]),
            "teama_tds_rush": int(stats.iloc[1, 1].split("-")[2]),
            "teama_tds_pass": int(stats.iloc[2, 1].split("-")[3]),
            "teama_tos": int(stats.iloc[7, 1]),
            "teama_4d_att": int(stats.iloc[10, 1].split("-")[1]),
            "teama_4d_comp": int(stats.iloc[10, 1].split("-")[0]),
            "teama_sacks": int(stats.iloc[3, 2].split("-")[0]),
            "teama_sack_yds": int(stats.iloc[3, 2].split("-")[1]),
            "teama_rtn_td": int(away_rtn_td),
            "teama_drives": int(away_drives),
            "teamh_name": points.iloc[1, 1],  # NOT INT
            "teamh_pts": int(points.iloc[1, -1]),
            "teamh_pts_q1": int(points.iloc[1, 2]),
            "teamh_pts_q2": int(points.iloc[1, 3]),
            "teamh_pts_q3": int(points.iloc[1, 4]),
            "teamh_pts_q4": int(points.iloc[1, 5]),
            "teamh_yds": int(stats.iloc[5, 2]),
            "teamh_yds_rush": int(stats.iloc[1, 2].split("-")[1]),
            "teamh_yds_pass": int(stats.iloc[2, 2].split("-")[2]),
            "teamh_tds": int(stats.iloc[1, 2].split("-")[2])
            + int(stats.iloc[2, 2].split("-")[3]),
            "teamh_tds_rush": int(stats.iloc[1, 2].split("-")[2]),
            "teamh_tds_pass": int(stats.iloc[2, 2].split("-")[3]),
            "teamh_tos": int(stats.iloc[7, 2]),
            "teamh_4d_att": int(stats.iloc[10, 2].split("-")[1]),
            "teamh_4d_comp": int(stats.iloc[10, 2].split("-")[0]),
            "teamh_sacks": int(stats.iloc[3, 1].split("-")[0]),
            "teamh_sack_yds": int(stats.iloc[3, 1].split("-")[1]),
            "teamh_rtn_td": int(home_rtn_td),
            "teamh_drives": int(home_drives),
        }
    )

    return game_dict


def get_games(cursor):
    """takes (cursor) and returns list of game ids not in db for CURRENT SEASON"""
    if dt.datetime.now().month >= 7:
        season = dt.datetime.now().year
    else:
        season = dt.datetime.now().year - 1
    url = "https://www.pro-football-reference.com/years/" + str(season) + "/games.htm"
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    db_games = [
        tup[0] for tup in cursor.execute("select match_id from raw;").fetchall()
    ]

    game_urls = []
    for link in soup.find_all("a"):
        # only games that have happened and have the boxscore text
        if link.text == "boxscore":
            if (
                re.findall("\d\d\d\d\d\d\d\d\d\D\D\D", link.get("href"))[0]
                not in db_games
            ):
                game_urls.append(
                    "https://www.pro-football-reference.com" + link.get("href")
                )
    return game_urls


def insert_row(conn, tablename, row_dict):
    """takes any dict and inserts it into a sql table with matching schema"""
    keys = ",".join(row_dict.keys())
    question_marks = ",".join(list("?" * len(row_dict)))
    values = tuple(row_dict.values())
    conn.execute(
        "INSERT INTO " + tablename + " (" + keys + ") VALUES (" + question_marks + ")",
        values,
    )


def update_db(cursor):
    """takes (cursor), updates DB with missing games from current season"""
    games = get_games(cursor)
    games_num = len(games)
    print(f"There are {games_num} games missing from this season")
    count_ = 1
    for game in games:
        game_id = re.findall("\d\d\d\d\d\d\d\d\d\D\D\D", game)[0]
        print(f"Scraping game {count_} of {games_num} ({game_id})")
        dict_ = scrape_game(game)
        insert_row(cursor, "raw", dict_)
        count_ += 1


def get_games_year(year, cursor):
    """takes (year, cursor) and pulls game ids not in db for a SPECIFIC SEASON"""
    url = "https://www.pro-football-reference.com/years/" + str(year) + "/games.htm"
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    db_games = [
        tup[0] for tup in cursor.execute("select match_id from raw;").fetchall()
    ]

    game_urls = []
    for link in soup.find_all("a"):
        # only games that have happened and have the boxscore text
        if link.text == "boxscore":
            if (
                re.findall("\d\d\d\d\d\d\d\d\d\D\D\D", link.get("href"))[0]
                not in db_games
            ):
                game_urls.append(
                    "https://www.pro-football-reference.com" + link.get("href")
                )
    return game_urls


def update_db_year(year, cursor):
    """takes (year, cursor), updates DB with missing games from given season"""
    games = get_games_year(year, cursor)
    games_num = len(games)
    print(f"There are {games_num} games missing from this season")
    count_ = 1
    for game in games:
        game_id = re.findall("\d\d\d\d\d\d\d\d\d\D\D\D", game)[0]
        print(f"Scraping game {count_} of {games_num} ({game_id})")
        dict_ = scrape_game(game)
        insert_row(cursor, "raw", dict_)
        count_ += 1
