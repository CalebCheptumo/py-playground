from django.shortcuts import render


def home(request):
    return render(request, 'meal_plans/home.html')