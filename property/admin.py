from django.contrib import admin

from .models import Flat, Complaint, Owner

class OwnerInline(admin.TabularInline):
    raw_id_fields = ('owner', )
    model = Owner.flats.through

@admin.register(Flat)
class AdminFlat(admin.ModelAdmin):
    search_fields = ['owner', 'address', 'town',]
    readonly_fields = ('created_at',)
    list_display = ('address', 'price', 'new_building', 'construction_year', 'town', 'owners_phonenumber', 'pure_owners_phonenumber')
    list_editable = ['new_building',]
    list_filter = ['new_building', 'rooms_number', 'has_balcony', 'active', 'town']
    raw_id_fields = ("likes",)
    inlines = [
        OwnerInline,
    ]

@admin.register(Complaint)
class AdminComplaint(admin.ModelAdmin):
    raw_id_fields = ("flat",)

@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('flats',)

