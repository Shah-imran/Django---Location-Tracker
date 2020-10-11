from django.shortcuts import redirect, render
from django.contrib import messages

def home(request):
    context = {
        
    }

    return render(request, "location/home.html", context)
