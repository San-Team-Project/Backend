# Generated by Django 2.0.4 on 2019-03-17 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0011_doctor_availabel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='hospitallink',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='portfoliolink',
            field=models.URLField(blank=True, null=True),
        ),
    ]
