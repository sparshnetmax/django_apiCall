import praw

testapp1 = {'cid': 'cc_iaxhXXfdEvQ',
            'Csecret': '8D16LS5H-Q_WycPBBKSBMufsI7E',
            'user_agent':"test by /u/sparsh3333",
            'redirectURI':'http://127.0.0.1:8000/redirect'}

testapp2 = {'cid': 'zGA-aW1QSCPewg',
            'Csecret': 'O2El3f1oUGfAUWFbcvJcseZbEsc',
            'user_agent':"script by /u/sparsh3333",
            'redirectURI':'http://127.0.0.1:8000/redirect'}
testapp1=testapp2


reddit_for_auth = praw.Reddit(client_id=testapp1['cid'],
                     client_secret=testapp1['Csecret'],
                     user_agent=testapp1['user_agent'],
                     redirect_uri=testapp1['redirectURI'])

def ref_token(token):
    answer = 'False'
    reddit_for_Refresh = praw.Reddit(client_id=testapp1['cid'],
                     client_secret=testapp1['Csecret'],
                     user_agent=testapp1['user_agent'],
                     refresh_token=token)
    try:
        answer= reddit_for_Refresh.auth.scopes()
        token = reddit_for_Refresh.auth
    except:
        answer= reddit_for_Refresh.read_only
    return answer
