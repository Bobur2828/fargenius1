# Generated by Django 5.0.6 on 2024-06-08 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='porfolio',
            name='client_description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='porfolio',
            name='client_name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]