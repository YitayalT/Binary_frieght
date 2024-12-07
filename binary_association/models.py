from django.db import models

class Association(models.Model):
    association_id = models.CharField(max_length=50, unique=True)
    start_date = models.DateField()
    role = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    description = models.TextField()
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    tin = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"Association {self.association_id} - {self.role}"

    class Meta:
        verbose_name = "Association"
        verbose_name_plural = "Associations"

class Owner(models.Model):
    full_name_or_company_name = models.CharField(max_length=255)
    owner_type = models.CharField(max_length=100, choices=[('Individual', 'Individual'), ('Company', 'Company')])
    address = models.CharField(max_length=500)
    national_id_number = models.CharField(max_length=50, unique=True)
    tin = models.CharField(max_length=20, unique=True)
    drivers_license_number = models.CharField(max_length=50, unique=True)
    date_of_birth = models.DateField()
    ownership_start_date = models.DateField()
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f"Owner: {self.full_name_or_company_name}"

    class Meta:
        verbose_name = "Owner"
        verbose_name_plural = "Owners"
        

class Car(models.Model):
    association = models.ForeignKey('Association', on_delete=models.CASCADE, related_name='cars')
    car_id = models.CharField(max_length=50, unique=True)
    owner = models.ForeignKey('Owner', on_delete=models.CASCADE, related_name='cars')
    insurance_provider = models.CharField(max_length=255)
    rental_period = models.DurationField()
    car_model = models.CharField(max_length=100)
    fuel_type = models.CharField(max_length=50, choices=[('Petrol', 'Petrol'), ('Diesel', 'Diesel'), ('Electric', 'Electric'), ('Hybrid', 'Hybrid')])
    cargo_type = models.CharField(max_length=100)
    cargo_capacity = models.PositiveIntegerField()  # Capacity in kilograms
    vehicle_age = models.PositiveIntegerField()  # Age in years

    def __str__(self):
        return f"Car {self.car_id} - {self.car_model}"

    class Meta:
        verbose_name = "Car"
        verbose_name_plural = "Cars"