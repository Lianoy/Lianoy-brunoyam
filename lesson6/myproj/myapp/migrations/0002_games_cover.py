# Generated by Django 4.2.7 on 2023-11-12 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='games',
            name='cover',
            field=models.ImageField(blank=True, upload_to='myapp/static/covers/'),
        ),
    ]