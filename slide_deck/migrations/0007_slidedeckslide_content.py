# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-15 10:53
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('slide_deck', '0006_remove_slidedeck_carousel'),
    ]

    operations = [
        migrations.AddField(
            model_name='slidedeckslide',
            name='content',
            field=wagtail.wagtailcore.fields.RichTextField(default=None),
            preserve_default=False,
        ),
    ]
