from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    if(request.GET and request.GET["pop_message"]):
        context = {"pop_message": request.GET["pop_message"]}
        return render(request, "pwadmin/index.html", context)
    else:
        return render(request, "pwadmin/index.html")

def login(request):
    return render(request, "pwadmin/login.html")

def handle_login(request):
    pop_message = "Usuário logado com sucesso"
    print(request.POST["user"])
    print(request.POST["password"])
    return HttpResponseRedirect(reverse("pwadmin:index") + "?pop_message=" + pop_message)