# Inside views.py in the questions project folder

from django.shortcuts import render

def landing_page(request):
    return render(request, 'landing_page.html')
