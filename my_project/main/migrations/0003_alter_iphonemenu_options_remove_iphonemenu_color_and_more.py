# Generated by Django 4.1.5 on 2023-03-29 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_iphonemenu_remove_iphone_photo2_remove_iphone_photo3'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='iphonemenu',
            options={'verbose_name': 'Mеню', 'verbose_name_plural': 'меню айфонов'},
        ),
        migrations.RemoveField(
            model_name='iphonemenu',
            name='color',
        ),
        migrations.RemoveField(
            model_name='iphonemenu',
            name='imgcolor',
        ),
        migrations.AddField(
            model_name='iphonemenu',
            name='sim',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='SIM1'),
        ),
        migrations.AddField(
            model_name='iphonemenu',
            name='sim2',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='SIM1'),
        ),
        migrations.AddField(
            model_name='iphonemenu',
            name='sim3',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='SIM1'),
        ),
        migrations.AddField(
            model_name='iphonemenu',
            name='size2',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Емкость'),
        ),
        migrations.AddField(
            model_name='iphonemenu',
            name='size3',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Емкость'),
        ),
        migrations.AddField(
            model_name='iphonemenu',
            name='size4',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Емкость'),
        ),
        migrations.AlterField(
            model_name='iphonemenu',
            name='size',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Емкость'),
        ),
    ]
