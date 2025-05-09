# Generated by Django 5.1.7 on 2025-04-12 08:35

from django.db import migrations

def create_owner (apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')

    for flat in Flat.objects.all():
        owner, _ = Owner.objects.get_or_create(name=flat.owner, phone=flat.owners_phonenumber,
                                    pure_phone=flat.pure_owners_phonenumber)
        owner.flats.add(flat)

class Migration(migrations.Migration):

    dependencies = [
        ('property', '0011_owner'),
    ]

    operations = [
        migrations.RunPython(create_owner),
    ]
