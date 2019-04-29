# Generated by Django 2.0.4 on 2019-03-16 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0003_specialist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='specialization',
        ),
        migrations.AddField(
            model_name='doctor',
            name='specialization',
            field=models.ManyToManyField(blank=True, to='doctor.Specialist'),
        ),
    ]
