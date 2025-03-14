# Generated by Django 5.1.3 on 2025-02-10 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_remove_propertyhistory_house_delete_houseimage_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='sell',
            name='built_year',
            field=models.IntegerField(blank=True, null=True, verbose_name='Built Year'),
        ),
        migrations.AddField(
            model_name='sell',
            name='ending_year',
            field=models.IntegerField(blank=True, null=True, verbose_name='Ending Year'),
        ),
        migrations.AddField(
            model_name='sell',
            name='starting_year',
            field=models.IntegerField(blank=True, null=True, verbose_name='Starting Year'),
        ),
        migrations.AddField(
            model_name='sell',
            name='usage_history',
            field=models.TextField(blank=True, null=True, verbose_name='Usage History (Who used the house?)'),
        ),
    ]
