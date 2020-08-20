import  praw
testapp1 = {'cid': 'zGA-aW1QSCPewg',
            'Csecret': 'O2El3f1oUGfAUWFbcvJcseZbEsc',
            'user_agent':"script by /u/sparsh3333",
            'redirectURI':'http://127.0.0.1:8000/redirect'}
reddit = praw.Reddit(client_id=testapp1['cid'],
                     client_secret=testapp1['Csecret'],
                     user_agent=testapp1['user_agent'],
refresh_token="606894205423-wZKoU21rdO_l2xx6iFOukUgTF5M",
                     )

user_info = dict()
user_info['name'] = reddit.user.me()
user_info['karma'] = reddit.user.karma()
for i,k in user_info.items():
    print(i,':',k)
