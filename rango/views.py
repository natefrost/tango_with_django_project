from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says hey there partner! \n <a href=http://127.0.0.1:8000/rango/about>the Rango about page</a>")

def about(request):#
    return HttpResponse("""Rango says here is the about page.
                        
    <a href=http://127.0.0.1:8000>click here to return to the index page</a>
    """)

