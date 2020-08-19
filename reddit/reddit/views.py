from django.shortcuts import redirect,render,HttpResponse
from django.http.response import JsonResponse
import json
from django.template import RequestContext
from .reditCreds import *
from django.contrib.sessions.models import Session


def redirectUri(request):
    code = request.GET['code']
    print(code)
    data = CreateRefToken(code,reddit_for_auth)
    data=dict(data)
    request.session['reddit_reftoken'] = data['code']
    request.session['acc_token'] = code
    return redirect('/')

def index(request):
    try:
        r_check= render(request, 'index.html')
        r_check.set_cookie('refreshToken',str(request.session['reddit_reftoken']))
        return JsonResponse({'accessToken':request.session['acc_token'],
                             'refreshToken':request.session['reddit_reftoken'],})

    except:
        return render(request, 'index.html')
def makeURL(request):
    url = reddit_for_auth.auth.url(["identity"], "permanent")

    request.session['redir_url'] = url
    return redirect(request.session['redir_url'])
def CreateRefToken(code,reddit):
    code = reddit.auth.authorize(code)
    data = {'code':code}
    return data


def newAccessToken(request):
    token = request.session['reddit_reftoken']
    info = ref_token(token)
    return HttpResponse(info)
    # return JsonResponse ({'token':newToken})

def exitFuction():
    Session.objects.all().delete()
    return redirect('/')