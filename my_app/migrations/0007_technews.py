# Generated by Django 2.2.2 on 2021-11-11 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0006_auto_20211110_1257'),
    ]

    operations = [
        migrations.CreateModel(
            name='Technews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('content', models.TextField()),
                ('image_url', models.CharField(blank=True, max_length=255)),
            ],
        ),
    ]
