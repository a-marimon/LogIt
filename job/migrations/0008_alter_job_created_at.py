# Generated by Django 3.2.23 on 2025-01-22 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0007_auto_20250122_2043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]
