# Generated by Django 2.2.2 on 2021-11-10 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0004_auto_20211110_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='address',
            field=models.CharField(blank=True, default='Not stated', max_length=100),
        ),
    ]