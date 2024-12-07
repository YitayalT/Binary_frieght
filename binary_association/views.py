from django.shortcuts import render
from .models import Car, Association, Owner

def car_list(request):
    # Fetch all cars from the database
    cars = Car.objects.all()

    # Pass the cars data to the template
    return render(request, 'binary_association/car_list.html', {'cars': cars})


def association_list(request):
    # Fetch all association details from the Association model
    associations = Association.objects.all()

    # Pass the association data to the template
    return render(request, 'binary_association/association_list.html', {'associations': associations})


def owner_list(request):
    # Fetch all owner details from the Owner model
    owners = Owner.objects.all()

    # Pass the owner data to the template
    return render(request, 'binary_association/owner_list.html', {'owners': owners})