# Generated by Django 5.0.6 on 2024-06-10 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0007_rename_category_porfolio_category_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='image',
        ),
        migrations.AddField(
            model_name='category',
            name='icon',
            field=models.ImageField(default=1, upload_to='Service/photo', verbose_name='Servis  ikon kiriting'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='photo',
            field=models.ImageField(default=1, upload_to='Service/photo', verbose_name='Portfolio rasmini kiriting'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='photo1',
            field=models.ImageField(blank=True, null=True, upload_to='Service/photo', verbose_name='Portfolio rasmini kiriting'),
        ),
        migrations.AddField(
            model_name='category',
            name='photo2',
            field=models.ImageField(blank=True, null=True, upload_to='Service/photo', verbose_name='Portfolio rasmini kiriting'),
        ),
        migrations.AddField(
            model_name='category',
            name='photo3',
            field=models.ImageField(blank=True, null=True, upload_to='Service/photo', verbose_name='Portfolio rasmini kiriting'),
        ),
        migrations.AddField(
            model_name='category',
            name='photo4',
            field=models.ImageField(blank=True, null=True, upload_to='Service/photo', verbose_name='Portfolio rasmini kiriting'),
        ),
        migrations.AddField(
            model_name='category',
            name='title',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
