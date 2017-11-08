from TwitterData.TwitterController.TwitterAPI import TimelineStatuses
# from TwitterData.DatabaseController import *
from TwitterData.DatabaseController.Database import Database
from TwitterData.DatabaseController.WriteToDatabase import WriteToDatabase
from TwitterData.DatabaseController.ReadFromDatabase import ReadFromDatabase

# Get a list of people that have been mentioned and then start the process over and over and over again.

FILTER = { 'user_mentions': { '$gt': [] } }


def mentions_loop():
    pass

def add_to_db(user, mentions):
    a =  {user : mentions}
    db_name = "data"
    collection_name = "mentions_map"

    coll = WriteToDatabase(db_name, collection_name)
    coll.add_data(a)


def user_mentions(user):
    """ Puts distinct user_mention values in a list"""
    mentions = TimelineStatuses(user).read_distinct("user_mentions")

    a = add_to_db(user, mentions)

    return mentions


if __name__ == "__main__":
    user_mentions("BarackObama")