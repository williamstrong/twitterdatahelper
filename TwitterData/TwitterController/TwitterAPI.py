
import json
from datetime import datetime

import twitter

from TwitterData.TwitterController.TwitterError import NoSubClass
from TwitterData.DatabaseController.Database import Database
from TwitterData.DatabaseController.ReadFromDatabase import ReadFromDatabase
from TwitterData.DatabaseController.WriteToDatabase import WriteToDatabase
from TwitterData.TwitterController import __credential_file__ as twitter_cred


def search_db(db_name, coll_name):
    if coll_name == None:
        raise NoSubClass
    db = Database(db_name)
    coll_list = db.collections()
    for x in coll_list:
        if x == coll_name:
            return True
    return False

class Tweets:
    def __init__(self):

        with open(twitter_cred, 'r') as file:
            auth_keys = json.load(file)
        self.CONSUMER_KEY = auth_keys["CONSUMER_KEY"]
        self.CONSUMER_SECRET = auth_keys["CONSUMER_SECRET"]
        self.OAUTH_TOKEN = auth_keys["OAUTH_TOKEN"]
        self.OAUTH_TOKEN_SECRET = auth_keys["OAUTH_TOKEN_SECRET"]

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
        self.collection = None

        self.db = WriteToDatabase("timeline_tweets")

    def request_tweets_from_api(self):
        # Test last_id; if exist start from last_id else start from beginning
        last_id = 0
        api_request = self._api_call()
        self._add_tweet_list_to_db(api_request)
        while len(api_request) > 1:
            try:
                last_id = api_request[-1].id
            except IndexError:
                pass
            try:
                api_request = self._tweets_since_last_id(last_id)
            except twitter.error.TwitterError as err:
                print(err)
                return
            self._add_tweet_list_to_db(api_request)

    def _add_tweet_list_to_db(self, tweet_list):
        for status in tweet_list:
            self.db.add_data(self.collection, status.AsDict())
        self._counter(tweet_list)
        # Potentially another way to do this
        # self.db.add_data([status.AsDict for status in tweet_list])

    def _counter(self, list):
        self.count += len(list)

    def _api_call(self):
        raise NoSubClass(type(self).__name__)

    def _tweets_since_last_id(self, last_id):
        raise NoSubClass(type(self).__name__)


class TimelineStatuses(ReadFromDatabase):
    def __init__(self, name):
        if not search_db("timeline_tweets", name): TimelineStatusesRS(name)
        super(TimelineStatuses, self).__init__("timeline_tweets", name)


        self.name = name
        self.db = ReadFromDatabase("timeline_tweets", self.name)

class TimelineStatusesRS(RequestAndStore):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.collection = name
        self.request_tweets_from_api()

    # If api call is needed
    def _api_call(self):
        return self.api.GetUserTimeline(
            screen_name=self.name,
            count=200,
            exclude_replies=True,
            trim_user=True)

    def _tweets_since_last_id(self, last_id):
        #     print("Made it to last id")
        return self.api.GetUserTimeline(
            screen_name=self.name,
            count=200,
            max_id=last_id,
            exclude_replies=True,
            trim_user=True)

class Subject:
    def __init__(self, subject):
        if not search_db("subjects", subject): SubjectRS(subject)

        self.subject = subject
        self.db = ReadFromDatabase("subject", self.subject)


class SubjectRS(RequestAndStore):
    def __init__(self, subject, date):
        super().__init__()
        self.subject = subject
        self.since_date = date
        self.collection = subject
        self.request_tweets_from_api()


    def _api_call(self):
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
    # test.request_tweets_from_api()
