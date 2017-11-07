import unittest
from TwitterData.TwitterController.TwitterAPI import *


@unittest.skip
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

@unittest.skip
class TestRequestAndStoreTweets(unittest.TestCase):

    def setUp(self):
        pass

    def test_request_tweets_from_api(self):
        pass

    def test_add_tweet_list_to_db(self):
        pass

    def tearDown(self):
        pass


class TestTimelineStatusesRS(unittest.TestCase):
    def setUp(self):
        self.tl_class = TimelineStatusesRS("@BarackObama")
        self.tl_class.name = "willdstrong_test"

        self.db = ReadFromDatabase("timeline_tweets")

    def tearDown(self):
        pass

    def test_request_tweet_from_api(self):
        self.tl_class.request_tweets_from_api()
        self.assertTrue(self.db.read_raw_data("willdstrong_test") != None)

@unittest.skip
class TestTimelineStatuses(unittest.TestCase):

    def setUp(self):
        self.db = Database("timeline_tweets")
        self.db.create_collection("test")

    def tearDown(self):
        self.db.remove_collection("test")


    def test_TimelineStatusesR(self):
        self.assertTrue(type(TimelineStatuses("test")) == TimelineStatusesR)

    def test_TimelineStatusesRS(self):
        self.assertTrue(type(TimelineStatuses("not_test")) == TimelineStatusesRS)




