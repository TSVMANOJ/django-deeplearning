# Generated by Django 4.0.4 on 2022-06-14 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aslapp', '0002_image_delete_imageset'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
