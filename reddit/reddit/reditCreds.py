import praw


testapp1={'cid' : 'cc_iaxhXXfdEvQ','Csecret' : '8D16LS5H-Q_WycPBBKSBMufsI7E'}
testapp2={'cid' : 'TSdf18VQt_wT-g'}
password = 'Spnetmax33'
username = 'sparsh3333'

reddit = praw.Reddit(client_id=testapp1['cid'],
                     client_secret=testapp1['Csecret'],
                     user_agent="test by /u/sparsh3333",
              redirect_uri='http://127.0.0.1:8000/redirect')

url=(reddit.auth.url(["identity"], "permanent"))
print(url)

def refToken(code):
    code = reddit.auth.authorize(code)
    data = {'code':code}
    return data

