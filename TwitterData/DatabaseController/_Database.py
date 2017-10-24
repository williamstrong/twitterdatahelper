from pymongo import MongoClient


class DB:

    def __init__(self):

        # For use with MongoDB Atlas
        with open("mongo_connect.txt") as mongo_cred_file:
            mongo_cred = mongo_cred_file.read()
        self.client = MongoClient(mongo_cred)


        # Connect to DB
        # self.client = MongoClient('localhost', 27017)
        # self.db = self.client.store_tweets

        # self.collection = self.db.tweet_collection

    def collect_stats(self):
        # print(self.db.command("collstats", "new"))
        pass

    def show_collections(self):
        print(self.db.collection_names())

    def search_collection_name(self, name):
        pass
