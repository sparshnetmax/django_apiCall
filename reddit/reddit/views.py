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

User = apps.get_model(app_label='redit_auth',model_name= 'User')


def redirectUri(request):
    code = request.GET['code']
    request.session['AccessToken'] = code
    print(code)
    data = CreateRefToken(code,reddit_for_auth)
    data=dict(data)
    request.session['reddit_reftoken'] = data['code']
    request.session['AppUser'] =str(data['user'])
    try:
        user1=User.objects.get(Appuser=request.session['AppUser'] )
        user1.refreshToken=request.session['reddit_reftoken']
        user1.save()
    except:
        user1=User(Appuser=request.session['AppUser'],
                   refreshToken=request.session['reddit_reftoken'])
        user1.save()
    return redirect('/')

def index(request):
    print(os.getcwd())
    connection = checker(request)
    if connection == False:
        request.session.delete()
        return redirect('/authenticate')


    result ={'refreshToken': request.session['reddit_reftoken'],'AppUser': request.session['AppUser'],'AccessToken':request.session['AccessToken']}
    cookie_token =HttpResponse('Cookie')
    cookie_token.set_cookie('token',str(request.session['reddit_reftoken']),'AppUser',str(request.session['AppUser']))
    writeFile(request,result)
    return JsonResponse(result)

def makeURL(request):
    url = reddit_for_auth.auth.url(scopes=scope_list, state="permanent")
    print(url)
    return redirect(url)
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

def exitFuction(request):
    Session.objects.all().delete()
    return redirect('/')
def userinfo(request):
    token = request.session['reddit_reftoken']
    info = reddit_for_auth.user.karma()
    print(info.values())
    return HttpResponse(info)
def checker(request):
    name = False
    try:
        ref_token = request.session['reddit_reftoken']
        reddit = praw.Reddit(client_id=testapp1['cid'],
                         client_secret=testapp1['Csecret'],
                         user_agent=testapp1['user_agent'],
                         refresh_token=ref_token)
        name = reddit.user.me()
        return name
    except:
        return name
def userPosts(request):
    reddit = praw.Reddit(client_id=testapp1['cid'],
                         client_secret=testapp1['Csecret'],
                         user_agent=testapp1['user_agent'],
                         refresh_token=request.session['reddit_reftoken'])
    allUserPosts = reddit.redditor("sparsh3333").top('all')


def writeFile(request,result):
    path_to_file = os.path.join(os.getcwd(),'tokens',request.session['AppUser']+'.xml')
    fW = dicttoxml.dicttoxml(result).decode()
    fil1 = open(path_to_file ,'w')
    fil1.write(fW)
    fil1.close()
    print('File Writen at - '+path_to_file)

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

def makePost(request):
    connection = checker(request)
    if connection == False:
        request.session.delete()
        return redirect('/authenticate')
    try:
        img_src=request.GET['img_src']
    except:
        # print('Using test image because no image_src in parameter')
        return JsonResponse({'ERROR':'give a img_src'})

        pass
    try:
        title=request.GET['title']
    except:
        return JsonResponse({'ERROR':'give a post title'})
    # try:
    #     text=request.GET['text']
    # except:
    #     return JsonResponse({'ERROR':'give a post text'})
    reddit = praw.Reddit(client_id=testapp1['cid'],
                         client_secret=testapp1['Csecret'],
                         user_agent=testapp1['user_agent'],
                         refresh_token=request.session['reddit_reftoken'],
                         )
    reddit.subreddit("memes").submit(title=title, url=img_src, nsfw=False)
    return redirect('/')