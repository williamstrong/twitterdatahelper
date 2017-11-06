from pymongo import MongoClient


class DB:

    def __init__(self):

        # For use with MongoDB Atlas
        with open("TwitterData/DatabaseController/mongo_connect") as mongo_cred_file:
            mongo_cred = mongo_cred_file.read()
        self.client = MongoClient(mongo_cred)
        self.db = self.client.tweets


        # Connect to DB
        # self.client = MongoClient('localhost', 27017)
        # self.db = self.client.store_tweets

        # self.collection = self.db.tweet_collection

    def create_collection(self, collection_name):
        self.db.create_collection(collection_name)

    def remove_collection(self, collection_name):
        """Dangerous, only use this if intending to permanently delete a collection."""
        self.db.drop_collection(collection_name)

    def collect_stats(self):
        # print(self.db.command("collstats", "new"))
        pass

    def show_collections(self):
        print(self.db.collection_names())

    def search_collection_name(self, name):
        pass

