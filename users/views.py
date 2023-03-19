from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .forms import CustomUserCreationForm
from .models import CustomUser

# Create your views here.

def index(request):
    form = CustomUserCreationForm
    users = CustomUser.objects.all()
    template = loader.get_template("users/index.html")
    return HttpResponse(
        template.render({"form": form, "users": users}, request=request),
        
    )


def create_user(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect('index')