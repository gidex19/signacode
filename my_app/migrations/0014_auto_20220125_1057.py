# Generated by Django 2.2.2 on 2022-01-25 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0013_interest_my_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='technews',
            name='image_url',
            field=models.CharField(default='https://media.istockphoto.com/photos/selective-focus-of-stacking-magazine-place-on-table-in-living-room-picture-id813136942?k=20&m=813136942&s=612x612&w=0&h=K9YYeYSORn8pz__9admNT1gI5paHSCwylAe7w4vL2D4=', max_length=255),
        ),
    ]