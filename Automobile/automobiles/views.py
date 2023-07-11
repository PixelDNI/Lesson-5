from django.shortcuts import render
from .models import Car
# Create your views here.

def input_form(request):
    # Car.objects.create(
    #     Car.brand =
    # )
    if request.method == 'POST':
        form_data = request.POST

        new_car = Car()
        new_car.brand = form_data['brand']
        new_car.year = form_data['year']
        new_car.color = form_data['color']
        new_car.mileage = form_data['mileage']
        new_car.cost = form_data['cost']

        new_car.save()


    return render(request, 'index.html')


def output_data(request):
    cars = Car.objects.all()
    context = {'cars':cars}

    return render(request, 'display.html', context=context)