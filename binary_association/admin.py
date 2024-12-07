from django.contrib import admin
from .models import Car
from .models import Association
from .models import Owner

# Custom Admin Site class
admin.site.site_header = 'Binary Freight Logistics Owner'
admin.site.site_title = 'Binary Freight Logistics Admin'
admin.site.index_title = 'Welcome to Binary Freight Logistics Admin Panel'
# Register your models with the custom admin site
# Example: admin_site.register(YourModel)
admin.site.register(Car)
admin.site.register(Owner)
admin.site.register(Association)






