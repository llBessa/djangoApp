from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "pwadmin/index.html")

def login(request):
    return render(request, "pwadmin/login.html")