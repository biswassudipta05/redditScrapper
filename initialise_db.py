# -*- coding: utf-8 -*-

# Coded by Sudipta Biswas
# biswassudipta05@gmail.com

# Script to initilize the database with the new tables

import sqlite3
import configparser
import traceback

try:
    config_data = configparser.ConfigParser()
    
    config_data.read("meta_config.ini")
    script_config = config_data.get("config_files","script_config")

    config_data.read(script_config)

    try:
        connection = sqlite3.connect(config_data.get("database","db_name"))
    except sqlite3.Error as error:
        print("Error connecting to the database",error)
        raise

    print("Opened database successfully")

    file_name = 'redditScrap.sql'

    # Will execute the script to create the tables
    with open(file_name, 'r') as sql_file:
        sql_script = sql_file.read()

    print("Script executed Succesfully")

    cursor = connection.cursor()
    cursor.executescript(sql_script)

except Exception:
    traceback.print_exc()
finally:
    connection.commit()
    connection.close()