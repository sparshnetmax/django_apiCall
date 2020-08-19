import praw
from requests import Session


def makeURL():
    testapp1={'cid' : 'cc_iaxhXXfdEvQ','Csecret' : '8D16LS5H-Q_WycPBBKSBMufsI7E'}

    password = 'Spnetmax33'
    username = 'sparsh3333'

    session = Session()
    session.verify = "certfile.pem"
    reddit = praw.Reddit(client_id=testapp1['cid'],
                         client_secret=testapp1['Csecret'],
                         user_agent="test by /u/sparsh3333",
                  redirect_uri='http://127.0.0.1:8000/')

    url=(reddit.auth.url(["identity"], "permanent"))
    return url