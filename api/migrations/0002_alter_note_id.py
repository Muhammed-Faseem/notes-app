# Generated by Django 4.1.5 on 2025-03-04 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='id',
            field=models.CharField(max_length=255, primary_key=True, serialize=False),
        ),
    ]
