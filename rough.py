def checker(token,request):
    try:
        reddit = praw.Reddit(client_id=testapp1['cid'],
                             client_secret=testapp1['Csecret'],
                             user_agent=testapp1['user_agent'],
                             refresh_token=token,
                             )
        user_info = dict()
        user_info['name'] = reddit.user.me()
        user_info['karma'] = reddit.user.karma()
        for i, k in user_info.items():
            print(i, ':', k)
        print(reddit.user.me())
    except:

        Session.objects.all().delete()
        CONNECTION_LOST=True
        print(request.session['reddit_reftoken'])
        print('SESSION CLEARED')