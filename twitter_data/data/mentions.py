from ..data import *

from twitter_data.twitter_controller.twitter_api import TimelineStatuses


from ..Utility import threaded
from threading import Lock




# Get a list of people that have been mentioned and then start the process over and over and over again.

FILTER = { 'user_mentions': { '$gt': [] } }
db_name = "data"
collection_name = "mentions_map"
db = ReadDb(db_name, collection_name)

# For testing
first_user = "BarackObama"

users = []
master_users = []

def recursive_from_first_user():
    w = user_list(first_user)
    master_users.append(first_user)
    w.join()

def master_users_init(fn):
    return fn()

def main(*args, **kwargs):
    master_users_init(args[0])
    # Will continue until it can't anymore. Will it download all of twitter? Who knows.
    while (more_users()):
        with user_lock:
            if user_not_in_master(users[0]):
                user_list(users[0])
                with master_lock:
                    master_users.append(users[0])
                del users[0]
            else:
                del users[0]


def more_users():
    with user_lock:
        return len(users) > 0


def user_not_in_master(user):
    with master_lock:
        return not user in master_users

def remove_duplicates(l):
    return list(set(l))

user_lock = Lock()
master_lock = Lock()

@threaded
def user_list(user):

    user_list = []
    mentions = user_mentions(user)

    for i in mentions:
        user_list.append(i["screen_name"])

    add_to_db(user, user_list)


def add_to_users(user_list):
    """Used for recursively getting user data"""
    with user_lock:
        for i in user_list:
            users.append(i)

def mentions_map_in_db(user):
    db.collection.find({user : {"$exist" : True}})

def add_to_db(user, mentions):
    a =  {user : mentions}

    coll = WriteDb(db_name, collection_name)
    coll.add_data(a)

def user_mentions(user):
    from twitter_data.twitter_controller.twitter_api import db_limit_lock
    """ Puts distinct user_mention values in a list"""
    with db_limit_lock:
        mentions = TimelineStatuses(user).read_distinct("user_mentions")

    return mentions


if __name__ == "__main__":
    main()
