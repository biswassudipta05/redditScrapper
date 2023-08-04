# -*- coding: utf-8 -*-

# Coded by Sudipta Biswas
# biswassudipta05@gmail.com

# Script to create a CSV report (Needs to be enhanced)

import csv
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

    cursor = connection.cursor()
    cursor.execute("""select date(max(run_date)) from dd_dates""")
    max_run_date = next(cursor, [None])[0]
    cursor.close()

    csv_name = 'Report_' + str(max_run_date) + '.csv'

    cursor = connection.cursor()
    cursor.execute("""select row_number() over(order by subRS desc) as Rank,
                    s.name Subreddit, f.subRS, date(d.run_date) 'Run Date'
                    from ft_subRS f, dd_subreddits s, dd_dates d
                    where date(d.run_date) = (select date(max(run_date)) from dd_dates)
                    and f.sub_id = s.sub_id
                    and d.date_key = f.date_key
                    order by rank;""")
    with open(csv_name, "w", newline='') as csv_file:   
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([i[0] for i in cursor.description]) # write headers
        csv_writer.writerows(cursor)

except Exception:
    traceback.print_exc()
finally:
    connection.close()