import twitter
from Database import DB


class Tweets:
    def __init__(self):
        self.CONSUMER_KEY = '***REMOVED***'
        self.CONSUMER_SECRET = '***REMOVED***'
        self.OAUTH_TOKEN = '***REMOVED***'
        self.OAUTH_TOKEN_SECRET = '***REMOVED***'

        self.api = twitter.Api(
            self.CONSUMER_KEY,
            self.CONSUMER_SECRET,
            self.OAUTH_TOKEN,
            self.OAUTH_TOKEN_SECRET,
            sleep_on_rate_limit=True)

        # Database initialization
        self.db = DB()

        # Statistics
        self.count = 0

    def check_rate_limit(self):
        self.api.InitializeRateLimit()
        print(self.api.rate_limit.resources)


class RequestAndStore(Tweets):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def request_tweets_from_api(self):
        #     Test last_id; if exist start from last_id else start from beginning
        last_id = 0
        tweets = self._new_tweets()
        self.add_tweet_list_to_db(tweets)
        while True:
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
            self.db.add_data(status.AsDict())
        print("Added to DB")
        self._counter(tweet_list)
        # Potentially another way to do this
        # self.db.add_data([status.AsDict for status in tweet_list])

    def _counter(self, list):
        self.count += len(list)
        print(self.count)

    def _new_tweets(self):
        pass

    def _tweets_since_last_id(self, last_id):
        pass


class RequestAndStoreTimelineStatuses(RequestAndStore):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def request_tweets_from_api(self):
        #     Test last_id; if exist start from last_id else start from beginning
        last_id = 0
        tweets = self._new_tweets()
        self.add_tweet_list_to_db(tweets)
        while True:
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
            self.db.add_data(status.AsDict())
        print("Added to DB")
        self._counter(tweet_list)
        # Potentially another way to do this
        # self.db.add_data([status.AsDict for status in tweet_list])

    def _counter(self, list):
        self.count += len(list)
        print(self.count)

    def _new_tweets(self):
        tweet_list = self.api.GetUserTimeline(
            screen_name=self.user,
            count=200,
            exclude_replies=True,
            trim_user=True)
        print("Got tweets")
        return tweet_list

    def _tweets_since_last_id(self, last_id):
        #     print("Made it to last id")
        tweets = self.api.GetUserTimeline(
            screen_name=self.user,
            count=200,
            max_id=last_id,
            exclude_replies=True,
            trim_user=True)
        print("Got tweets")
        return tweets


class RequestAndStoreSubject(RequestAndStore):
    def __init__(self, subject, date):
        super().__init__()
        self.subject = subject
        self.since_date = date

    def request_tweets_from_api(self):
        GetSearch(self,
                  term=self.subject,
                  since_id=None,
                  max_id=None,
                  until=None,
                  since=self.since_date,
                  count=200,
                  lang=None,
                  locale=None,
                  result_type="mixed",
                  include_entities=None)

if __name__ == "__main__":
    test = RequestAndStore()
    test.request_tweets_from_api()
