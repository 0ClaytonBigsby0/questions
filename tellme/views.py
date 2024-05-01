from django.shortcuts import render

def tell_me(request):
    return render(request, 'tellme/tellme.html')

def tell_me2(request):
    return render(request, 'tellme/tellme2.html')