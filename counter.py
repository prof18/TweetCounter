import twint

from db_handler import DBHandler

db_handler = DBHandler()



# c = twint.Config()
# c.Search = "#DevFest1Veneto"
#
# twint.run.Search(c)
#
#
# def jobone():
# 	print ("Fetching Tweets")
# 	c = twint.Config()
# 	# choose username (optional)
# 	c.Username = "insert username here"
# 	# choose search term (optional)
# 	c.Search = "insert search term here"
# 	# choose beginning time (narrow results)
# 	c.Since = "2018-01-01"
# 	# set limit on total tweets
# 	c.Limit = 1000
# 	# no idea, but makes the csv format properly
# 	c.Store_csv = True
# 	# format of the csv
# 	c.Custom = ["date", "time", "username", "tweet", "link", "likes", "retweets", "replies", "mentions", "hashtags"]
# 	# change the name of the csv file
# 	c.Output = "filename.csv"
# 	twint.run.Search(c)