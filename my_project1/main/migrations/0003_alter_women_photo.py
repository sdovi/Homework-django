# Generated by Django 4.1.5 on 2023-03-26 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_women_alter_airpods_create_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='women',
            name='photo',
            field=models.ImageField(upload_to='main/img/'),
        ),
    ]
