# Generated by Django 5.0.3 on 2024-05-12 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_alter_employee_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='employee_location',
        ),
    ]
