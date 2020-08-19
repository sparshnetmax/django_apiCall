from django.shortcuts import redirect,render,HttpResponse
from django.http.response import JsonResponse
import json
from .reditCreds import *

def redirectUri(request):
    code = request.GET['code']
    print(code)
    data = CreateRefToken(code,request.session['reddit_creds'])
    data=dict(data)
    return JsonResponse(data)

def index(request):
    return render(request, 'index.html')

def signIn(request):
    url,reddit = makeURL()
    request.session['redir_url'] = url
    request.session['reddit_creds'] = reddit
def makeURL():
    reddit = praw.Reddit(client_id=testapp1['cid'],
                         client_secret=testapp1['Csecret'],
                         user_agent=testapp1['user_agent'],
                         redirect_uri=testapp1['redirectURI'])
    url = (reddit.auth.url(["identity"], "permanent"))
    return url,reddit
def CreateRefToken(code,reddit):
    code = reddit.auth.authorize(code)
    data = {'code':code}
    return data
