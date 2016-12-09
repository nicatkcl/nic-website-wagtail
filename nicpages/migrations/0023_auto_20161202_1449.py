# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-02 14:49
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('nicpages', '0022_revealjspage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='revealjspage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField([('slide', wagtail.wagtailcore.blocks.StreamBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock()), (b'caption', wagtail.wagtailcore.blocks.CharBlock())]))], blank=True, null=True),
        ),
    ]