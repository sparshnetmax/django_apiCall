from django.shortcuts import redirect,render,HttpResponse
from django.http.response import JsonResponse
import json
from django.template import RequestContext
from django.apps import apps
from .reditCreds import *
from django.contrib.sessions.models import Session

User = apps.get_model(app_label='redit_auth',model_name= 'User')

def redirectUri(request):
    code = request.GET['code']
    print(code)
    data = CreateRefToken(code,reddit_for_auth)
    data=dict(data)
    request.session['reddit_reftoken'] = data['code']
    request.session['acc_token'] = code
    user = User.objects.get(id=request.session['id'])
    user.refreshToken = data['code']
    user.save()
    request.session['AppUser'] =str(data['user'])
    return redirect('/')

def index(request):
    connection = checker(request)
    if connection == False:
        request.session.delete()
        return redirect('/authenticate')
    try:
        return JsonResponse({'accessToken': request.session['acc_token'],
                             'refreshToken': request.session['reddit_reftoken'],
                             'AppUser': request.session['AppUser']})
    except:
        return JsonResponse({'ERROR 404':'Invalid login'})
def makeURL(request):
    try:
        uname=request.GET['username']
        password=request.GET['password']
        try:
            user1 = User.objects.get(username=uname)
            db_passwrd = user1.password
        except:
            user1 = 0
        if user1 !=0:
            if password == db_passwrd:
                login=True
                request.session['user'] = uname
                request.session['password'] = password
                request.session['id'] = user1.id
                request.session['refreshToken'] = user1.refreshToken
            else:
                print(db_passwrd)
                return JsonResponse({'ERROR 500 L1': 'Incorrect password'})
        else:
            return JsonResponse({'ERROR 500 L1': 'Username does not exist'})
    except:
        return JsonResponse({'ERROR 500':'LOGIN NEEDED (Please login using your USERNAME and PASSWORD)'})
    url = reddit_for_auth.auth.url(scopes=scope_list, state="permanent")

    request.session['redir_url'] = url
    return redirect(request.session['redir_url'])
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

    # return JsonResponse ({'token':newToken})

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
        user = User.objects.get(id=request.session['id'])
        ref_token = user.refreshToken


        reddit = praw.Reddit(client_id=testapp1['cid'],
                         client_secret=testapp1['Csecret'],
                         user_agent=testapp1['user_agent'],
                         refresh_token=ref_token)
        name = reddit.user.me()
        return name
    except:
        return name
