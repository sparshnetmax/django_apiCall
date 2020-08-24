# def checker(token,request):
#     try:
#         reddit = praw.Reddit(client_id=testapp1['cid'],
#                              client_secret=testapp1['Csecret'],
#                              user_agent=testapp1['user_agent'],
#                              refresh_token=token,
#                              )
#         user_info = dict()
#         user_info['name'] = reddit.user.me()
#         user_info['karma'] = reddit.user.karma()
#         for i, k in user_info.items():
#             print(i, ':', k)
#         print(reddit.user.me())
#     except:
#
#         Session.objects.all().delete()
#         CONNECTION_LOST=True
#         print(request.session['reddit_reftoken'])
#         print('SESSION CLEARED')
testapp1 = {'cid': 'zGA-aW1QSCPewg',
            'Csecret': 'O2El3f1oUGfAUWFbcvJcseZbEsc',
            'user_agent':"script by /u/sparsh3333",
            'redirectURI':'http://127.0.0.1:8000/redirect'}

scope_list = ['account', 'creddits', 'edit', 'flair', 'history', 'identity', 'livemanage',
              'modconfig', 'modcontributors', 'modflair', 'modlog', 'modothers', 'modposts',
              'modself', 'modwiki', 'mysubreddits', 'privatemessages', 'read', 'report', 'save',
              'submit', 'subscribe', 'vote', 'wikiedit', 'wikiread']

dict1 ={"refreshToken": "606894205423-m_WFi8nvohncLgtC24Dw6LcTKIQ", "AppUser": "sparsh3333", "AccessToken": "SiIr3eX9u6MFgX9ATByFbKMKdFU"}
import praw

reddit = praw.Reddit(client_id=testapp1['cid'],
                             client_secret=testapp1['Csecret'],
                             user_agent=testapp1['user_agent'],
                             refresh_token='606894205423--CwWU3IIfn93bAh3jn5QKQQWltI',

                             )
img_src = 'https://cdn.vox-cdn.com/thumbor/kcwYR08QGJ5Srb-Z_VY8bXp01SI=/0x0:1920x1080/1200x800/filters:focal(807x387:1113x693)/cdn.vox-cdn.com/uploads/chorus_image/image/59245045/hangoutsscreen_3.0.jpg'
allUserPosts = reddit.redditor("sparsh3333").top('all')
# print(allUserPosts)
reddit.subreddit("memes").submit(title="my meme title", url=img_src, nsfw=False,)

