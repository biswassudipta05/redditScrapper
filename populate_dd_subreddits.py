# -*- coding: utf-8 -*-

# Coded by Sudipta Biswas
# biswassudipta05@gmail.com

# Script to Populate DD_SUBREDDITS

import sqlite3
import praw
from prawcore import NotFound
import configparser
import traceback

def sub_exists(sub):
    exists = True
    try:
        reddit.subreddits.search_by_name(sub, exact=True)
    except NotFound:
        exists = False
    return exists

def insert_dd_subreddit(subrname):
    for subr in subrname:
        if sub_exists(subr):
            submission = reddit.subreddit(str(subr))
            sub_id = submission.fullname #gives the fullname id for the subreddit
            sub_name = submission.display_name
            sub_title = submission.title
            cur = connection.cursor() 
            sql_query = "INSERT INTO dd_subreddits VALUES(?, ?, ?)"     
            sql_data = (sub_id, sub_name, sub_title)
            
            
            try:
                cur.execute(sql_query, sql_data)
                connection.commit() #commit after each record of subreddit is inserted
                print("Subreddit %s inserted successfully" % sub_name)
            except sqlite3.Error as er:
                print('SQLite error: %s' % (' '.join(er.args)))
        else:
            print("Invalid Subreddit Name")

try:
    config_data = configparser.ConfigParser()

    config_data.read("meta_config.ini")
    api_secrets_config = config_data.get("config_files","api_secrets_config")
    script_config = config_data.get("config_files","script_config")

    config_data.read(api_secrets_config)
    api_secrets = config_data["api_secrets"]

    reddit = praw.Reddit(client_id = api_secrets.get("client_id"),
                        client_secret = api_secrets.get("client_secret"),
                        user_agent = api_secrets.get("user_agent"),
                        username = api_secrets.get("username"),
                        password = api_secrets.get("password"))

    config_data.read(script_config)

    try:
        connection = sqlite3.connect(config_data.get("database","db_name"))
    except sqlite3.Error as error:
        print("Error connecting to the database",error)
        raise

    sub_list =  ((config_data.get("subreddits","sub_list")).replace('\n','')).split(',')

    insert_dd_subreddit(sub_list)

except Exception:
    traceback.print_exc()
finally:
    connection.close()
