# Generated by Django 5.1.3 on 2025-02-10 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_houseimage_propertyhistory'),
    ]

    operations = [
        migrations.AddField(
            model_name='sell',
            name='bathrooms',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sell',
            name='bedrooms',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
