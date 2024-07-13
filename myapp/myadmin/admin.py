from django.contrib import admin
from .models import Restaurant
# Register your models here.

class Restaurant_admin(admin.ModelAdmin):
    list_display =('name','location','items','full_details')
    list_filter=('name','location')
    search_fields=('name','location','items','full_details')


# Register your models here.
admin.site.register(Restaurant,Restaurant_admin)
