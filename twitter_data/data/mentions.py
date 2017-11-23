from threading import Lock

from twitter_data.Utility import threaded
from twitter_data.data import *
from twitter_data.twitter_controller.twitter_api import TimelineStatuses


# Global names for
DB_NAME = "data"
COLLECTION_NAME = "mentions_map"
DB = None


def db_init():
    DB = ReadDb(DB_NAME, COLLECTION_NAME)



USERS = []
MASTER_USERS = []


USER_LOCK = Lock()
MASTER_LOCK = Lock()



# List of initialization functions for the MASTER_USERS list.
def _recursive_from_first_user(first_user):
    w = _user_list(first_user)
    MASTER_USERS.append(first_user)
    w.join()


def _from_static_list(user_list):
    for user in user_list:
        USERS.append(user)


def _users_list_init(*args, **kwargs):
    return args[0](**kwargs)


def _main(*args, **kwargs):
    # Initialize USERS according to function passed in args[0] with parameters **kwargs
    _users_list_init(args[0], **kwargs)

    # Initialize DB as a ReadDB instance using the globals variable DB_NAME and COLLECTION_NAME
    db_init()

    #
    while (_more_users()):
        with USER_LOCK:
            if _user_not_in_master(USERS[0]):
                _user_list(USERS[0])
                with MASTER_LOCK:
                    MASTER_USERS.append(USERS[0])
                del USERS[0]
            else:
                del USERS[0]


def _more_users():
    with USER_LOCK:
        return len(USERS) > 0


def _user_not_in_master(user):
    with MASTER_LOCK:
        return not user in MASTER_USERS


def _remove_duplicates(l):
    return list(set(l))


@threaded
def _user_list(user):
    user_list = []
    mentions = _user_mentions(user)

    for i in mentions:
        user_list.append(i["screen_name"])

    _add_to_db(user, user_list)


def _add_to_users(user_list):
    """Used for recursively getting user data"""
    with USER_LOCK:
        for i in user_list:
            USERS.append(i)


def _mentions_map_in_db(user):
    DB.collection.find({user: {"$exist": True}})


def _add_to_db(user, mentions):
    a = {'user': user, 'user_mentions': mentions}

    coll = WriteDb(DB_NAME, COLLECTION_NAME)
    coll.add_data(a)


def _user_mentions(user):
    from twitter_data.twitter_controller.twitter_api import db_limit_lock
    """ Puts distinct user_mention values in a list"""
    with db_limit_lock:
        mentions = TimelineStatuses(user).read_distinct("user_mentions")

    return mentions


"""
:param
"""


def _trim_network(collection):
    trimmed_network = DB.db[collection].aggregate([
        {"$unwind": "$user_mentions"},
        {"$lookup": {"from": collection, "localField": "user_mentions", "foreignField": "user", "as": "validUser"}},
        {"$match": {"validUser.user": {"$exists": "true"}}},
        {
            "$group": {
                "_id": "$_id",
                "user": {"$first": "$user"},
                "user_mentions": {"$push": "$user_mentions"}
            }
        }])
    return trimmed_network


def self_contained_network(untrimmed_collection, trimmed_collection, type=_from_static_list, user_list=_user_list,
                           database='data'):
    # Redefine global variables DB_NAME and COLLECTION_NAME.
    DB_NAME = database
    COLLECTION_NAME = untrimmed_collection

    # Main function for creating database entries with users mentioned users.
    _main(type, user_list=user_list)

    # Trim and put trimmed entries into a trimmed_collection.
    trim = _trim_network(untrimmed_collection)
    from twitter_data.database_controller import WriteToDatabase
    w_db = WriteToDatabase(database, trimmed_collection)
    for doc in trim:
        w_db.add_data(doc)
    return ReadDb(database, trimmed_collection)


if __name__ == "__main__":
    # from twitter_data.data import congress
    # main(from_static_list, user_list=congress.congress_users())

    trim = _trim_network("congress_map")
    from twitter_data.database_controller import WriteToDatabase

    w_db = WriteToDatabase("data", "congress_map_trimmed")
    for doc in trim:
        w_db.add_data(doc)
