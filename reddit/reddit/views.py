from django.shortcuts import redirect,render,HttpResponse
from django.http.response import JsonResponse
import json
from django.template import RequestContext
from django.apps import apps
from .reditCreds import *
from django.contrib.sessions.models import Session

User = apps.get_model(app_label='redit_auth',model_name= 'User')
def checker(token):
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
        print('SESSION CLEARED')
        return redirect('/')
def redirectUri(request):
    code = request.GET['code']
    print(code)
    data = CreateRefToken(code,reddit_for_auth)
    data=dict(data)
    request.session['reddit_reftoken'] = data['code']
    request.session['acc_token'] = code
    request.session['AppUser'] =str(data['user'])
    return redirect('/')

def index(request):
    try:
        ref_token_to_use =request.session['reddit_reftoken']
        print(ref_token_to_use)
        checker(ref_token_to_use)
    except:
        pass

    try:
        # r_check= render(request, 'index.html')
        # r_check.set_cookie('refreshToken',str(request.session['reddit_reftoken']))

        return JsonResponse({'accessToken':request.session['acc_token'],
                             'refreshToken':request.session['reddit_reftoken'],
                             'AppUser':request.session['AppUser']})
    except:
        return render(request, 'index.html')
def makeURL(request):
    try:
        uname=request.GET['username']
        password=request.GET['password']
        try:
            user1 = User.objects.get(username='sparsh')
            db_passwrd = user1.password
        except:
            user1 = 0
        if user1 !=0:
            if password == db_passwrd:
                login=True
            else:
                return JsonResponse({'ERROR 500 L1': 'Incorrect password'})
        else:
            return JsonResponse({'ERROR 500 L1': 'Username does not exist'})
    except:
        return JsonResponse({'ERROR 500':'LOGIN NEEDED (Please login using your USERNAME and PASSWORD)'})
    url = reddit_for_auth.auth.url(scopes=scope_list, state="permanent")
    request.session['user'] = uname
    request.session['password'] = password
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