# Generated by Django 4.1.5 on 2023-03-29 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_menuwatch_imgcolor10'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='iphonemenu',
            name='content',
        ),
        migrations.RemoveField(
            model_name='iphonemenu',
            name='imgcolor2',
        ),
        migrations.RemoveField(
            model_name='iphonemenu',
            name='imgcolor3',
        ),
        migrations.RemoveField(
            model_name='iphonemenu',
            name='imgcolor4',
        ),
        migrations.RemoveField(
            model_name='iphonemenu',
            name='imgcolor5',
        ),
        migrations.RemoveField(
            model_name='iphonemenu',
            name='list',
        ),
        migrations.RemoveField(
            model_name='iphonemenu',
            name='photoiphone',
        ),
        migrations.RemoveField(
            model_name='iphonemenu',
            name='sim',
        ),
        migrations.RemoveField(
            model_name='iphonemenu',
            name='sim2',
        ),
        migrations.RemoveField(
            model_name='iphonemenu',
            name='sim3',
        ),
        migrations.RemoveField(
            model_name='iphonemenu',
            name='size',
        ),
        migrations.RemoveField(
            model_name='iphonemenu',
            name='size2',
        ),
        migrations.RemoveField(
            model_name='iphonemenu',
            name='size3',
        ),
        migrations.RemoveField(
            model_name='iphonemenu',
            name='size4',
        ),
        migrations.AddField(
            model_name='iphone',
            name='content',
            field=models.TextField(max_length=256, null=True, verbose_name='описание'),
        ),
        migrations.AddField(
            model_name='iphone',
            name='imgcolor2',
            field=models.ImageField(null=True, upload_to='img'),
        ),
        migrations.AddField(
            model_name='iphone',
            name='imgcolor3',
            field=models.ImageField(null=True, upload_to='img'),
        ),
        migrations.AddField(
            model_name='iphone',
            name='imgcolor4',
            field=models.ImageField(null=True, upload_to='img'),
        ),
        migrations.AddField(
            model_name='iphone',
            name='imgcolor5',
            field=models.ImageField(null=True, upload_to='img'),
        ),
        migrations.AddField(
            model_name='iphone',
            name='list',
            field=models.TextField(max_length=2706, null=True, verbose_name='Описание продукта'),
        ),
        migrations.AddField(
            model_name='iphone',
            name='photoiphone',
            field=models.ImageField(null=True, upload_to='img', verbose_name='фото Айфона'),
        ),
        migrations.AddField(
            model_name='iphone',
            name='sim',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='SIM'),
        ),
        migrations.AddField(
            model_name='iphone',
            name='sim2',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='SIM2'),
        ),
        migrations.AddField(
            model_name='iphone',
            name='sim3',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='SIM3'),
        ),
        migrations.AddField(
            model_name='iphone',
            name='size',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Емкость'),
        ),
        migrations.AddField(
            model_name='iphone',
            name='size2',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Емкость2'),
        ),
        migrations.AddField(
            model_name='iphone',
            name='size3',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Емкость3'),
        ),
        migrations.AddField(
            model_name='iphone',
            name='size4',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Емкость4'),
        ),
    ]
