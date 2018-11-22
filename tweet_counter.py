from datetime import datetime

import pandas as pd
import twint

from db_handler import DBHandler
from twitter_params import TwitterParams

initialize_tweet_table = False
mine_new_tweets = False

# DB Stuff
db_handler = DBHandler()
db = db_handler.db_connection()
cursor = db.cursor()

# Twitter Params
word_to_search = 'DevFest1Veneto'
users_to_exclude = ['gdgvenezia', 'marcoGomier']
twitter_params = TwitterParams(word_to_search, users_to_exclude)

if initialize_tweet_table:
    print('Initializing Tweets table')
    cursor.execute(db_handler.drop_tweet_table_query)
    cursor.execute(db_handler.init_tweet_table_query)
    db.commit()

if mine_new_tweets:
    twint.run.Search(twitter_params.get_config())

    # Save the tweets as Dataframe
    tweets = twint.storage.panda.Tweets_df
    tweets = tweets[['id', 'username', 'name', 'user_id', 'tweet', 'created_at']]

    for tweet_value in tweets.values:
        id = tweet_value[0]
        username = tweet_value[1]
        fullname = tweet_value[2]
        user_id = tweet_value[3]
        content = tweet_value[4]
        timestamp = tweet_value[5]

        date = datetime.fromtimestamp(timestamp / 1e3)
        int_date = int(date.strftime('%Y%m%d'))

        if username not in twitter_params.user_to_exclude:

            existing_tweets = pd.read_sql(sql=db_handler.check_tweet_query, con=db, params=(id,))
            if existing_tweets.empty:
                print('Inserting tweet {} to db'.format(id))
                params = (id, username, fullname, user_id, timestamp, content)
                cursor.execute(db_handler.insert_tweet_table, params)
                db.commit()

# Print top users
top_users = pd.read_sql(sql=db_handler.top_users_query, con=db)
print(top_users.iloc[:10])
