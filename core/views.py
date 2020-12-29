from django.shortcuts import render

# Create your views here.

def index(req):

    return render(req,'core/index.htm',{'home':'active'})

def contact(req):
    return render(req,'core/contact.htm',{'contact':'active'})
