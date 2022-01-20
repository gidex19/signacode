# Generated by Django 2.2.2 on 2022-01-05 10:04

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0003_auto_20211223_1354'),
    ]

    operations = [
        migrations.AddField(
            model_name='learn_js',
            name='overview',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='learn_js',
            name='resources',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='learn_js',
            name='task_and_projects',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='product_type',
            field=models.CharField(choices=[('Learn Js', 'Learn Js'), ('Learn Python', 'Learn Python'), ('Digital Marketing', 'Digital Marketing'), ('Blockchain', 'Blockchain')], max_length=100),
        ),
    ]