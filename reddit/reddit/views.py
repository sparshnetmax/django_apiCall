from django.shortcuts import redirect,render,HttpResponse
from django.http.response import JsonResponse
from django.apps import apps
from .reditCreds import *
from django.contrib.sessions.models import Session
from django.contrib.sessions.backends.db import SessionStore
import dicttoxml
import os
from django.template import RequestContext
from django.core.serializers.json import Serializer

def redirectUri(request): # The redirct url that is added into developer app .This url gives us the code returned from redit portal
    code = request.GET['code']
    request.session['AccessToken'] = code
    print(code)
    data = CreateRefToken(code,reddit_for_auth) #Function to get refresh token
    data=dict(data)
                                # MAKING SESSION and Database entries
    request.session['reddit_reftoken'] = data['code']
    request.session['AppUser'] =str(data['user'])
    return redirect('/')        #redirecting to main page after authenticating the session

def index(request):
    #Home Page
    connection = checker(request)    #Function to check the pemissions of the user
    if connection == False:
        request.session.delete()
        return redirect('/authenticate')  #If permisiions revoked the user get redirected to main login for new token
    result ={'refreshToken': request.session['reddit_reftoken'],'AppUser': request.session['AppUser'],'AccessToken':request.session['AccessToken']}
    cookie_token =HttpResponse('Cookie')
    cookie_token.set_cookie('token',str(request.session['reddit_reftoken']),'AppUser',str(request.session['AppUser']))
    return JsonResponse(result)  #Render of page with json respose conating credentials. User info  and token

def makeURL(request):            #Funtion to call URL for app permissions
    url = reddit_for_auth.auth.url(scopes=scope_list, state="permanent")
    print(url)
    return redirect(url)         #Redirected to redit app with client id and secret

#FUNTION TO MAKE REFRESH TOKEN
def CreateRefToken(code,reddit):
    code = reddit.auth.authorize(code)
    user = reddit.user.me()
    print(user)
    data = {'code':code,'user':user}
    return data


def newAccessToken(request):
    token = request.session['reddit_reftoken']
    info,reddit = ref_token(token)
    return HttpResponse(info)

#FUNCTION TO KILL THE SESSION
def exitFuction(request):
    Session.objects.all().delete()
    return redirect('/')

#FUNCTION TO GET USER INFO
def userinfo(request):
    token = request.session['reddit_reftoken']
    connection = checker(request)  # Function to check the pemissions of the user
    if connection == False:
        request.session.delete()
        return redirect('/authenticate')  # If permisiions revoked the user get redirected to main login for new token
    reddit = praw.Reddit(client_id=testapp1['cid'],
                         client_secret=testapp1['Csecret'],
                         user_agent=testapp1['user_agent'],
                         refresh_token=token,
                         )
    info = {'name':str(reddit.user.me()),'karma':str(reddit.user.karma())}

    print(info.items())
    return HttpResponse(info.items())

#FUNCTION TO CHECK THE PERMISIONS OF THE USER
def checker(request):
    name = False
    try:
        ref_token = request.session['reddit_reftoken']
        reddit = praw.Reddit(client_id=testapp1['cid'],
                         client_secret=testapp1['Csecret'],
                         user_agent=testapp1['user_agent'],
                         refresh_token=ref_token)
        name =str( reddit.user.me())
        print('HELLO - ' + name)
        return name
    except:
        return False
# #FUNTION TO GET USER POSTS FORM REDIT
# def userPosts(request):
#     #MAKING REDIT INSTANCE USING EXISTING REFRESH TOKEN
#     reddit = praw.Reddit(client_id=testapp1['cid'],
#                          client_secret=testapp1['Csecret'],
#                          user_agent=testapp1['user_agent'],
#                          refresh_token=request.session['reddit_reftoken'])
#     allUserPosts = reddit.redditor("sparsh3333").top('all')
#     return HttpResponse(allUserPosts)

#FUNTION TO WRITE USER INFO INTO XML FILE



#FUNTION TO GET USER POSTS FORM REDIT
def show_post(request):
    connection = checker(request)
    if connection == False:
        request.session.delete()
        return redirect('/authenticate')
    data_list = list()
    reddit = praw.Reddit(client_id=testapp1['cid'],
                         client_secret=testapp1['Csecret'],
                         user_agent=testapp1['user_agent'],
                         refresh_token=request.session['reddit_reftoken'],
                         )
    allUserPosts = reddit.redditor(request.session['AppUser']).top('all')
    print(allUserPosts)
    for i in allUserPosts:
        print(vars(i))
        data_list.extend([{'title':i.title, 'text':i.selftext_html, 'author':str(i.author),'id':i.id}])
    return JsonResponse({'type':'post','data': data_list},safe=False,json_dumps_params=None)

#FUNTION TO MAKE USER POSTS FORM REDIT
def makePost(request):
    connection = checker(request)     #CHECKING CONNECTION
    if connection == False:
        request.session.delete()
        return redirect('/authenticate')
    try:                                        #PROVIDE IMAGE AND TITLE IN THE URL
        img_src=request.GET['img_src']
    except:

        return JsonResponse({'ERROR':'give a img_src'})

        pass
    try:
        title=request.GET['title']
    except:
        return JsonResponse({'ERROR':'give a post title'})

    reddit = praw.Reddit(client_id=testapp1['cid'],client_secret=testapp1['Csecret'],
                         user_agent=testapp1['user_agent'],refresh_token=request.session['reddit_reftoken'])
    reddit.subreddit("memes").submit(title=title, url=img_src, nsfw=False)
    return redirect('/')


