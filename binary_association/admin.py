from django.contrib import admin
from .models import Car
from .models import Association
from .models import Owner

# Custom Admin Site class
admin.site.site_header = 'Binary Freight Logistics Owner'
admin.site.site_title = 'Binary Freight Logistics Admin'
admin.site.index_title = 'Welcome to Binary Freight Logistics Admin Panel'
# Register your models with the custom admin site

class AssociationAdmin(admin.ModelAdmin):
    # Specify the attributes to display as columns
    list_display = ('association_id','start_date','role','location','description', 'phone_number','email', 'tin')
    # Optionally, add search and filter capabilities
    search_fields = ('association_id', 'role', 'location', 'email')
    list_filter = ('start_date', 'location')
    
class CarAdmin(admin.ModelAdmin):
    list_display = (
        'car_id',
        'association',  # Association as a related field
        'owner',        # Owner as a related field
        'insurance_provider',
        'rental_period',
        'car_model',
        'fuel_type',
        'cargo_type',
        'cargo_capacity',
        'vehicle_age',
    )

    # Optionally, add search and filter capabilities
    search_fields = ('car_id', 'car_model', 'owner__full_name_or_company_name', 'association__association_id')
    list_filter = ('fuel_type', 'cargo_type', 'vehicle_age', 'association', 'owner')
    
class OwnerAdmin(admin.ModelAdmin):
    # Specify the attributes to display as columns
    list_display = (
        'full_name_or_company_name',
        'owner_type',
        'address',
        'national_id_number',
        'tin',
        'drivers_license_number',
        'date_of_birth',
        'ownership_start_date',
        'phone_number',
    )

    # Optionally, add search and filter capabilities
    search_fields = ('full_name_or_company_name', 'national_id_number', 'tin', 'phone_number')
    list_filter = ('owner_type', 'ownership_start_date')
    
admin.site.register(Car, CarAdmin)
admin.site.register(Owner, OwnerAdmin)
admin.site.register(Association, AssociationAdmin)







