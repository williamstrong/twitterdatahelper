import unittest
from TwitterData.DatabaseController._Database import DB


class DatabaseControllerTest(unittest.TestCase):
    def setUp(self):
        self.db = DB()
        self.name = "Database(MongoClient(host=['twitterdata-shard-00-00-ojpbc.mongodb.net:27017', 'twitterdata-shard-00-01-ojpbc.mongodb.net:27017', 'twitterdata-shard-00-02-ojpbc.mongodb.net:27017'], document_class=dict, tz_aware=False, connect=True, ssl=True, replicaset='TwitterData-shard-0', authsource='admin'), 'name')"


    # insure connection is open to the proper database
    def connection_open(self):
        self.assertTrue(str(self.db.client.name) == self.name)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()