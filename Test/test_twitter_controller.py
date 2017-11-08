import unittest
from TwitterData.TwitterController.TwitterAPI import *


# @unittest.skip
class TestTweets(unittest.TestCase):

    def setUp(self):
        self.db = Database("test")
        self.db.create_collection("test")
        self.collection_search = "test"

        self.tweets = Tweets().api

    def test_api(self):
        self.assertTrue(self.tweets != None)

    def test_check_rate_limit(self):
        self.assertTrue(self.tweets.rate_limit)

    def test_search_db(self):
        self.assertTrue(search_db("test", self.collection_search))

    def tearDown(self):
        self.db.client.drop_database("test")



# @unittest.skip
class TestTimelineStatusesRS(unittest.TestCase):
    def setUp(self):
        self.tl_class = TimelineStatusesRS("willdstrong")
        self.tl_class.collection = "willdstrong_test"

        self.db = ReadFromDatabase("timeline_tweets", "willdstrong_test")

    def tearDown(self):
        pass

    def test_request_tweet_from_api(self):
        self.tl_class.request_tweets_from_api()
        self.assertTrue(self.db.read_raw_data() != None)

# @unittest.skip
class TestTimelineStatuses(unittest.TestCase):
    def setUp(self):
        self.timeline = TimelineStatuses("willdstrong")

    def test_db(self):
        self.assertTrue(self.timeline.db != None)


@unittest.skip
class TestSubjectRS(unittest.TestCase):
    def setUp(self):
        self.tl_class = SubjectRS("willdstrong")
        self.tl_class.collection = "willdstrong_test"

        self.db = ReadFromDatabase("timeline_tweets", "willdstrong_test")

    def tearDown(self):
        pass

    def test_request_tweet_from_api(self):
        self.tl_class.request_tweets_from_api()
        self.assertTrue(self.db.read_raw_data() != None)
