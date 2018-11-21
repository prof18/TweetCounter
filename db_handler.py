import MySQLdb

import configparser


class DBHandler:

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
