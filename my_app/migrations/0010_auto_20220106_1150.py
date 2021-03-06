# Generated by Django 2.2.2 on 2022-01-06 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0009_learn_fullstack'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='blockchain_level',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='customuser',
            name='business_level',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='customuser',
            name='fullstack_level',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='customuser',
            name='js_level',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='customuser',
            name='python_level',
            field=models.IntegerField(default=1),
        ),
    ]
