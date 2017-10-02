from pymongo import MongoClient


class DB:

    def __init__(self):

        self.username = 'twittermongo'
        self.password = 'i76L0kkCOlJZ6DtB'

        # Connect to DB
        self.client = MongoClient('localhost', 27017)
        self.db = self.client.store_tweets

        self.collection = self.db.tweet_collection

        self.posts = self.db.new7
        pass

    def add_data(self, data):
        '''
        
        :param data: dict of twitter data
        :return: id of document added to Mongodb
        '''
        post_id = self.posts.insert_one(data).inserted_id
        return post_id

    def add_data_to_new_collection(self, name, data):
        '''
        
        :param name: name of MongoDB collection
        :param data: dict of twitter data
        :return: 
        '''
        pass

    def CollStats(self):
        print(self.db.command("collstats", "new"))