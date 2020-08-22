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

dict1 ={"refreshToken": "606894205423-m_WFi8nvohncLgtC24Dw6LcTKIQ", "AppUser": "sparsh3333", "AccessToken": "SiIr3eX9u6MFgX9ATByFbKMKdFU"}

import dicttoxml
fW=dicttoxml.dicttoxml(dict1).decode()
fil1 = open('file1.xml','w')
fil1.write(fW)
fil1.close()