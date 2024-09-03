from django.shortcuts import render

def car_diagram(request):
    return render(request, 'cardiagram/car_diagram.html')