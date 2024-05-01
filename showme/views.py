from django.shortcuts import render

def show_me(request):
    return render(request, 'showme/showme.html')
