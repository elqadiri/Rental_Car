from django.contrib import admin
from .models import Car , ContactMessage

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('name', 'review', 'price_per_day', 'seats', 'transmission', 'fuel_type', 'year', 'gearbox', 'mileage')
    list_filter = ('transmission', 'fuel_type', 'year')
    search_fields = ('name', 'fuel_type')

admin.site.register(ContactMessage)
