# Generated by Django 5.0.3 on 2024-05-12 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_employee_employee_department_employee_employee_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='id',
            field=models.CharField(max_length=500, primary_key=True, serialize=False, unique='true'),
        ),
    ]
