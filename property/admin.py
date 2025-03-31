from django.contrib import admin

from .models import Flat

@admin.register(Flat)
class AdminFlat(admin.ModelAdmin):
    search_fields = ['owner', 'address', 'town',]
    readonly_fields = ('created_at',)
    list_display = ('address', 'price', 'new_building', 'construction_year', 'town',)
    list_editable = ['new_building',]

