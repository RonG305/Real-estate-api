# Generated by Django 4.2.2 on 2023-07-08 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='houses',
            name='house_image',
        ),
    ]