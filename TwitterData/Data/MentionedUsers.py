from ..DatabaseController.Read import ReadFromDatabase


# Get a list of people that have been mentioned and then start the process over and over and over again.

FILTER = { 'user_mentions': { '$gt': [] } }


def user_mentions(user):
    user_tweets = ReadFromDatabase("timeline_tweets", user)
    mention_tweets = user_tweets.read_filtered_data(FILTER)
    mentioned = []
    for i in mention_tweets:
        mentioned += i['user_mentions']
    return mentioned