from django.shortcuts import render

# Create your views here.

def index(req):
    return render(req,'serv/skill.htm',{"skill":"active"})