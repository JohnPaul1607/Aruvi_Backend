# Generated by Django 4.1.5 on 2023-01-17 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aruviapp', '0010_alter_student_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Date_of_birth',
            field=models.DateField(max_length=8),
        ),
    ]
