# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-26 15:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_auto_20180226_0206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image1',
            field=models.ImageField(blank=True, default='w.jpg', null=True, upload_to='', verbose_name='Profil'),
        ),
        migrations.AlterField(
            model_name='post',
            name='img1',
            field=models.ImageField(blank=True, default='w.jpg', upload_to='', verbose_name='İmg 1'),
        ),
        migrations.AlterField(
            model_name='post',
            name='img2',
            field=models.ImageField(blank=True, default='w.jpg', upload_to='', verbose_name='İmg 2'),
        ),
        migrations.AlterField(
            model_name='post',
            name='img3',
            field=models.ImageField(blank=True, default='w.jpg', upload_to='', verbose_name='İmg 3'),
        ),
    ]
