import os
# from social_networks.twitter_controller.twitter_api import TimelineStatuses, Subject

# __all__ = [TimelineStatuses, Subject]

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

__credential_file__ = os.path.join(__location__, "twitter_access.json")