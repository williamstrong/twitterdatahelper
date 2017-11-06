import unittest
from TwitterData.DatabaseController._Database import DB


class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.db = DB()
        self.name = "Database(MongoClient(host=['twitterdata-shard-00-00-ojpbc.mongodb.net:27017', 'twitterdata-shard-00-01-ojpbc.mongodb.net:27017', 'twitterdata-shard-00-02-ojpbc.mongodb.net:27017'], document_class=dict, tz_aware=False, connect=True, ssl=True, replicaset='TwitterData-shard-0', authsource='admin'), 'name')"


    # insure connection is open to the proper database
    def test_connection_open(self):
        self.assertTrue(str(self.db.client.name) == self.name)

    def test_create_collection(self):
        self.db.create_collection("test")
        self.assertTrue(in_list(self.db.show_collections()))

    def test_remove_collection(self):
        self.db.remove_collection("test")
        self.assertFalse(in_list(self.db.show_collections()))

    def tearDown(self):
        pass

def in_list(collection_list):
    """Return true if test is in collection"""
    if "test" in str(collection_list): return True
    else: return False


if __name__ == '__main__':
    unittest.main()