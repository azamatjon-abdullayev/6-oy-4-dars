# Generated by Django 5.1.2 on 2024-12-08 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='image',
            field=models.ImageField(default=11, upload_to='myfiles/photos/'),
            preserve_default=False,
        ),
    ]