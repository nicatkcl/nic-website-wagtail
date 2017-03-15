# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-14 17:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('slide_deck', '0003_slidedeckslide_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='slidedeckslide',
            name='transition',
            field=models.CharField(choices=[('none', 'none'), ('fade', 'fade'), ('slide', 'slide'), ('convex', 'convex'), ('concave', 'concave'), ('zoom', 'zoom')], default='none', max_length=50),
        ),
        migrations.AlterField(
            model_name='slidedeckslide',
            name='slide',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='slide', to='slide_deck.SlideDeck'),
        ),
    ]
