from django.shortcuts import render
from .forms import ContactFrm
from .models import ContactModal
# Create your views here.

def index(req):

    return render(req,'core/index.htm',{'home':'active'})

def contact(req):
    if req.method == "POST":
        cnFrm = ContactFrm(req.POST)
        if cnFrm.is_valid():
           name  = cnFrm.cleaned_data['name']
           email = cnFrm.cleaned_data['email']
           sub   = cnFrm.cleaned_data['subject']
           msg   = cnFrm.cleaned_data['msg']
           InsTble = ContactModal(name=name,email=email,sub=sub,msg=msg)
           InsTble.save()
           cnFrm = ContactFrm()
           return render(req,'core/contact.htm',{'contact':'active',"form":cnFrm,"msg":"Request Send Succcessfully,Our Team Contact Very Soon."})
        else:
            return render(req,'core/contact.htm',{'contact':'active',"form":cnFrm})
    else:
        cnFrm = ContactFrm()
        return render(req,'core/contact.htm',{'contact':'active',"form":cnFrm})
