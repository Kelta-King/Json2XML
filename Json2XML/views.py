from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from json2xml import json2xml
from json2xml.utils import readfromurl, readfromstring, readfromjson
import feedparser
import json

def home_page(request):
     return render(request, 'index.html', {
        'foo': 'bar',
    })

@csrf_exempt
def urlJson(request):
    try:
        data = json.loads(request.body)
        data = readfromurl(data['url'])
        print(json2xml.Json2xml(data).to_xml())
        return HttpResponse(json2xml.Json2xml(data).to_xml())    
    except Exception as e:
        print("An exception occurred", str(e))
        return HttpResponse(str(e))
    
@csrf_exempt
def textJson(request):
    try:
        data = json.loads(request.body)
        data = readfromstring(data['text'])
        print(json2xml.Json2xml(data).to_xml())
        return HttpResponse(json2xml.Json2xml(data).to_xml())    
    except Exception as e:
        print("An exception occurred", str(e))
        return HttpResponse(str(e))
    
