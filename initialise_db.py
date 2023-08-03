# -*- coding: utf-8 -*-

# Coded by Sudipta Biswas
# biswassudipta05@gmail.com

# Script to initilize the database with the new tables

import sqlite3
import configparser

config_data = configparser.ConfigParser()
config_data.read("config.ini")

db = sqlite3.connect(config_data.get("database","db_name"))

print("Opened database successfully")

file_name = 'redditScrap.sql'

# Will execute the script to create the tables
with open(file_name, 'r') as sql_file:
    sql_script = sql_file.read()

print("Script executed Succesfully")

cursor = db.cursor()
cursor.executescript(sql_script)
db.commit()
db.close()