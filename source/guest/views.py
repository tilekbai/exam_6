from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from guest.models import Guestbook

# Create your views here.

from django.shortcuts import render

def index_view(request):
    guests = Guestbook.objects.filter(status='active').order_by('-create_time')
    return render(request, 'index.html', context={'guests': guests})

def add_guest_view(request):
    if request.method == "GET":
        return render(request, 'add_guest.html')
    elif request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        text = request.POST.get("text")

        guest = Guestbook.objects.create(
            name=name,
            email=email,
            text=text,
        )

        guests = Guestbook.objects.filter(status='active').order_by('-create_time')
        return render(request, 'index.html', context={'guests': guests})