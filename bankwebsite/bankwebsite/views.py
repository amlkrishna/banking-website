from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def register(request):
    return render(request, 'register.html')

def index(request):
    return render(request, 'index.html')

def next_page(request):
        return render(request, 'nextpage.html')

def register(request):
    return render(request, 'register.html')

def last_page(request):
    return render(request, 'lastpage.html')