# Generated by Django 5.1.3 on 2025-02-11 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_remove_sell_ending_year_remove_sell_starting_year_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sell',
            name='house_type',
            field=models.CharField(choices=[('single_family', 'Single Family House'), ('villa', 'Villa'), ('farmhouse', 'Farmhouse'), ('land', 'Land'), ('apartment', 'Apartment'), ('condo', 'Condo'), ('townhouse', 'Townhouse'), ('bungalow', 'Bungalow'), ('duplex', 'Duplex'), ('penthouse', 'Penthouse'), ('studio', 'Studio'), ('cottage', 'Cottage'), ('mansion', 'Mansion')], max_length=50),
        ),
    ]
