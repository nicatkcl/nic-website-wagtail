# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-05 15:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import slide_deck.models
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0030_index_on_pagerevision_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='SlideDeckPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('body', wagtail.wagtailcore.fields.StreamField([('slide', wagtail.wagtailcore.blocks.StructBlock([(b'image', wagtail.wagtailcore.blocks.StructBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False))])), (b'transition', slide_deck.models.SlideTransitionChoiceBlock()), (b'slide_content', wagtail.wagtailcore.blocks.RichTextBlock()), (b'sub_slide', wagtail.wagtailcore.blocks.StreamBlock([(b'subslide_image', wagtail.wagtailcore.blocks.StructBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False))])), (b'subslide_content', wagtail.wagtailcore.blocks.RichTextBlock())]))]))], blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
