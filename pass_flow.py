import  praw
testapp1 = {'cid': 'zGA-aW1QSCPewg',
            'Csecret': 'O2El3f1oUGfAUWFbcvJcseZbEsc',
            'user_agent':"script by /u/sparsh3333",
            'redirectURI':'http://127.0.0.1:8000/redirect'}
reddit = praw.Reddit(client_id=testapp1['cid'],
                     client_secret=testapp1['Csecret'],
                     user_agent=testapp1['user_agent'],
refresh_token="606894205423-m_WFi8nvohncLgtC24Dw6LcTKIQ" )
me = reddit.user.me()
print(reddit.redditor('sparsh3333').hot())
