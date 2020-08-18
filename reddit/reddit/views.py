from django.shortcuts import redirect,render,HttpResponse
from django.http.response import JsonResponse

import json
from reddit.reditCreds import refToken
def redirectUri(request):
    code = request.GET['code']
    print(code)
    data = refToken(code)
    data=dict(data)
    return JsonResponse(data)

def index(request):
    return render(request, 'index.html')
