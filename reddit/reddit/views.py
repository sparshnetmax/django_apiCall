from django.shortcuts import redirect,render,HttpResponse
import json
from reddit.reditCreds import refToken
def redirectUri(request):
    code = request.GET['code']
    data = refToken(code)
    return HttpResponse(json.dumps(data))

def index(request):

    return render(request, 'index.html')
