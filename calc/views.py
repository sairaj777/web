from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return render(request,"home.html", {'names': 'dev'})

def check(request):
    name = request.GET.get('name', '')
    try :
        (type(name)==str )
        output = "welcome " + name
        return render(request,"result.html", {'result' : output})
    except Exception as e:
        print ("Plese enter a string")
    finally:
        print ("closed")