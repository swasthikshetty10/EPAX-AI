# Generated by Django 3.1.5 on 2021-04-06 08:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Mainapp', '0005_auto_20210406_1349'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notes',
            name='id',
        ),
        migrations.AlterField(
            model_name='notes',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, primary_key=True, serialize=False),
        ),
    ]
