
import json
from datetime import datetime

import twitter

from .TwitterError import NoSubClass
from ..DatabaseController.Write import WriteToDB


class Tweets:
    def __init__(self):
        file = "twitter_access.json"

        auth_keys = json.load(open(file, 'r'))
        self.CONSUMER_KEY = auth_keys["CONSUMER_KEY"]
        self.CONSUMER_SECRET = auth_keys["CONSUMER_SECRET"]
        self.OAUTH_TOKEN = auth_keys["OAUTH_TOKEN"]
        self.OAUTH_TOKEN_SECRET = auth_keys["OAUTH_TOKEN_SECRET"]

        # except FileNotFoundError:
        #     self.CONSUMER_KEY = ''
        #     self.CONSUMER_SECRET = ''
        #     self.OAUTH_TOKEN = ''
        #     self.OAUTH_TOKEN_SECRET = ''

        self.api = twitter.Api(
            self.CONSUMER_KEY,
            self.CONSUMER_SECRET,
            self.OAUTH_TOKEN,
            self.OAUTH_TOKEN_SECRET,
            sleep_on_rate_limit=True)

        # Statistics
        self.count = 0

    def check_rate_limit(self):
        self.api.InitializeRateLimit()
        print(self.api.rate_limit.resources)


class RequestAndStore(Tweets):
    def __init__(self):
        super().__init__()
        self.collection = "dump"
        self.db = WriteToDB()

    def request_tweets_from_api(self):
        #     Test last_id; if exist start from last_id else start from beginning
        last_id = 0
        tweets = self._new_tweets()
        self.add_tweet_list_to_db(tweets)
        while len(tweets) > 1:
            try:
                last_id = tweets[-1].id
            except IndexError:
                pass
            try:
                tweets = self._tweets_since_last_id(last_id)
            except twitter.error.TwitterError as err:
                print(err)
                return
            self.add_tweet_list_to_db(tweets)

    def add_tweet_list_to_db(self, tweet_list):
        for status in tweet_list:
            self.db.add_data(self.collection, status.AsDict())
        self._counter(tweet_list)
        # Potentially another way to do this
        # self.db.add_data([status.AsDict for status in tweet_list])

    def _counter(self, list):
        self.count += len(list)
        print(self.count)

    def _new_tweets(self):
        raise NoSubClass(type(self).__name__)

    def _tweets_since_last_id(self, last_id):
        raise NoSubClass(type(self).__name__)


class TimelineStatuses(RequestAndStore):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.collection = name + str(datetime.now())

    def _new_tweets(self):
        tweet_list = self.api.GetUserTimeline(
            screen_name=self.name,
            count=200,
            exclude_replies=True,
            trim_user=True)
        print("Got tweets")
        return tweet_list

    def _tweets_since_last_id(self, last_id):
        #     print("Made it to last id")
        tweets = self.api.GetUserTimeline(
            screen_name=self.name,
            count=200,
            max_id=last_id,
            exclude_replies=True,
            trim_user=True)
        print("Got tweets")
        return tweets


class Subject(RequestAndStore):
    def __init__(self, subject, date):
        super().__init__()
        self.subject = subject
        self.since_date = date
        self.collection = subject + date

    def _new_tweets(self):
        return self.api.GetSearch(
            term=self.subject,
            since=self.since_date,
            count=200)

    def _tweets_since_last_id(self, last_id):
        return self.api.GetSearch(
            term=self.subject,
            since=self.since_date,
            count=200)



if __name__ == "__main__":
    test = TimelineStatuses("willdstrong")
    test.request_tweets_from_api()
