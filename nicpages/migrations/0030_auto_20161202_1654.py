# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-02 16:54
from __future__ import unicode_literals

from django.db import migrations
import nicpages.models
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('nicpages', '0029_auto_20161202_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='revealjspage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField([('slide', wagtail.wagtailcore.blocks.StructBlock([(b'image', wagtail.wagtailcore.blocks.StructBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False))])), (b'transition', nicpages.models.SlideTransitionChoiceBlock()), (b'slide_content', wagtail.wagtailcore.blocks.RichTextBlock()), (b'sub_slide', wagtail.wagtailcore.blocks.StreamBlock([(b'image', wagtail.wagtailcore.blocks.StructBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False))])), (b'slide_content', wagtail.wagtailcore.blocks.RichTextBlock())]))]))], blank=True, null=True),
        ),
    ]
