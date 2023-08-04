# redditScrapper

redditScrapper is a little project coded using python and can be used to scrap data for subreddits, posts and comments and make simple CSV report from the data

## Installation

Make sure you have python3 with the [PRAW](https://pypi.org/project/praw/) module installed

## Usage

### Initial Setup

1. First get the API secrets for Reddit (you'll need a Reddit account for that). Modify `api_secrets.ini` with the appropriate values.

    >**`api_secrets.ini`**
    >``` ini
    >[api_secrets]
    >client_id = #Replace with client_id from reddit app
    >client_secret = #Replace with client_secret from reddit app
    >user_agent = #Replace with User agent, use anything e.g. redditScrap0.0.1
    >username = #Replace with Reddit Username
    >password = #Replace with Reddit Password
    >```

   You can change the default configs like Database name/location, limits and subreddit list using the `config.ini`

   Currently the subreddit list is the Top 50 SFW subreddits with the most Comments per day taken from [subredditstats.com](https://subredditstats.com/)

   If you want to use multiple config files for testing and development you can change the default config file names in `meta_config.ini`

2. Run `initialise_db.py` to create the DB and all the tables

3. Run `populate_dd_subreddits.py` to populate the table **`dd_subreddits`** with all the subreddits mentioned in config file

### Usual Run

Run `redditScrapper.py` to fetch data from Reddit using the subreddits present in the table **`dd_subreddits`** and populate the data into the respective tables

Run `generate_daily_report.py` to generate a simple daily report in CSV for the top ranking subreddits for the lastest day's data present in the DB.