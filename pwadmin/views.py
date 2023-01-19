from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    if(request.GET and request.GET["popmessage"]):
        context = {"popmessage": request.GET["popmessage"]}
        return render(request, "pwadmin/index.html", context)
    else:
        return render(request, "pwadmin/index.html")

def login(request):
    return render(request, "pwadmin/login.html")

def passwords(request):
    return render(request, "pwadmin/passwords.html")

def handle_login(request):
    pop_message = "Usuário logado com sucesso"
    pop_type = "success"
    print(request.POST["user"])
    print(request.POST["password"])
    return HttpResponseRedirect(f"{reverse('pwadmin:index')}?popmessage={pop_message}&poptype={pop_type}")