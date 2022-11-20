from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def handle_not_found(request, exception):
    return render(request, 'errors/not_found.html')