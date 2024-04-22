from django.shortcuts import render

# Create your views here.

def home(request):
    d={'info':"Hello my name is JACK"}
    return render(request,"home.html",context=d)
