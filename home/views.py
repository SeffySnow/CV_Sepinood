from django.shortcuts import render
from django.http import HttpResponse
from home.models import Message
from home.notifications import send_sms

def home(request):
    return render(request , "home.html")


def submit(request):
    if request.method == "POST":
        name = request.POST["name"]
        fname = request.POST["family"]
        email = request.POST["email"]
        t = request.POST["title"]
        text = request.POST["text"]
        try :
            Message.objects.create(
                name = name,
                lastname = fname,
                email = email,
                title = t,
                text = text,
            )
            send_sms(t)
    
            return render(request , "submitted.html", {'error':False})
        except:
            return render(request , "submitted.html",{'error':True})
    else:
        return HttpResponse('Data not Posted')
    
    