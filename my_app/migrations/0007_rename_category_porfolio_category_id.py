# Generated by Django 5.0.6 on 2024-06-10 20:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0006_about_image_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='porfolio',
            old_name='category',
            new_name='category_id',
        ),
    ]