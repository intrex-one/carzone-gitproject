# Generated by Django 4.2 on 2023-04-14 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_alter_car_features'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='tramsmission',
            new_name='transmission',
        ),
    ]
