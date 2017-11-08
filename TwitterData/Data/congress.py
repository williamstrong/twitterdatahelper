import pickle

with open('congress.pickle', 'rb') as f:
    congress_users = pickle.load(f)

tmp = []

for i in congress_users:
    tmp.append({i['screen_name']: i['name']})