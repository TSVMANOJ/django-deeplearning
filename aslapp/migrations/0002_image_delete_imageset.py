# Generated by Django 4.0.4 on 2022-06-14 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aslapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
        migrations.DeleteModel(
            name='ImageSet',
        ),
    ]
