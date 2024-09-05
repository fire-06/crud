# Generated by Django 5.1 on 2024-09-05 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='image',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='phone',
            name='lte_exists',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='phone',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='phone',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='phone',
            name='release_date',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='phone',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]