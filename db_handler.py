import MySQLdb

import configparser


class DBHandler:
    drop_tweet_table_query = "DROP TABLE IF EXISTS tweets"
    init_tweet_table_query = "CREATE TABLE tweets (" \
                             "tweet_id varchar(255) NOT NULL DEFAULT '', " \
                             "tweet_author_username varchar(255) NOT NULL DEFAULT ''," \
                             "tweet_author_fullname varchar(255) NOT NULL DEFAULT ''," \
                             "tweet_author_id varchar(255) NOT NULL DEFAULT ''," \
                             "tweet_date bigint(20) NOT NULL, " \
                             "tweet_content text DEFAULT NULL," \
                             "PRIMARY KEY (tweet_id)" \
                             ") ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;"
    insert_tweet_table = "INSERT INTO tweets (tweet_id, tweet_author_username, tweet_author_fullname, tweet_author_id, " \
                         "tweet_date, tweet_content) VALUES (%s, %s, %s, %s, %s, %s)"
    check_tweet_query = "SELECT * FROM tweets where tweet_id = %s"
    top_users_query = "select `tweet_author_username`,`tweet_author_fullname`, count(*) as tweet_number from tweets " \
                      "group by `tweet_author_username`, `tweet_author_fullname` order by tweet_number desc;"

    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config.ini')

        self.host = config['DB']['DB_HOST']
        self.user = config['DB']['DB_USER']
        self.pwd = config['DB']['DB_PWD']
        self.db = config['DB']['DB']

    def db_connection(self):
        """
            Returns the connection to the db
        """
        return MySQLdb.connect(host=self.host,
                               user=self.user,
                               passwd=self.pwd,
                               db=self.db,
                               use_unicode=True,
                               charset="utf8mb4")
