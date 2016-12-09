# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-02 14:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import nicpages.models
import wagtail.contrib.table_block.blocks
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtaildocs.blocks
import wagtail.wagtailembeds.blocks
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0030_index_on_pagerevision_created_at'),
        ('nicpages', '0021_auto_20161202_1336'),
    ]

    operations = [
        migrations.CreateModel(
            name='RevealJSPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('body', wagtail.wagtailcore.fields.StreamField([('h1', wagtail.wagtailcore.blocks.CharBlock(icon='title')), ('h2', wagtail.wagtailcore.blocks.CharBlock(icon='title')), ('h3', wagtail.wagtailcore.blocks.CharBlock(icon='title')), ('h4', wagtail.wagtailcore.blocks.CharBlock(icon='title')), ('h5', wagtail.wagtailcore.blocks.CharBlock(icon='title')), ('headline', nicpages.models.HeadlineBlock()), ('centre_heading', nicpages.models.CentreAlignHeadingBlock()), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('image_responsive', wagtail.wagtailcore.blocks.StructBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock())])), ('doc_with_preview', wagtail.wagtailcore.blocks.StructBlock([(b'preview', wagtail.wagtailimages.blocks.ImageChooserBlock()), (b'doc', wagtail.wagtaildocs.blocks.DocumentChooserBlock())])), ('home_video', nicpages.models.HomePageVideoBlock(icon='media')), ('equipment_banner_row', wagtail.wagtailcore.blocks.StructBlock([(b'first_image', wagtail.wagtailcore.blocks.StructBlock([(b'title', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False))])), (b'second_image', wagtail.wagtailcore.blocks.StructBlock([(b'title', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False))]))])), ('google_map', wagtail.wagtailcore.blocks.StructBlock([(b'title', wagtail.wagtailcore.blocks.CharBlock(max_length=255, required=True)), (b'street', wagtail.wagtailcore.blocks.CharBlock(max_length=255, required=True)), (b'postcode', wagtail.wagtailcore.blocks.CharBlock(max_length=255, required=True)), (b'city', wagtail.wagtailcore.blocks.CharBlock(max_length=255, required=True)), (b'map_long', wagtail.wagtailcore.blocks.CharBlock(max_length=255, required=True)), (b'map_lat', wagtail.wagtailcore.blocks.CharBlock(max_length=255, required=True)), (b'map_zoom_level', wagtail.wagtailcore.blocks.CharBlock(default=14, max_length=3, required=True)), (b'width', wagtail.wagtailcore.blocks.IntegerBlock(required=True)), (b'height', wagtail.wagtailcore.blocks.IntegerBlock(required=True))])), ('two_columns', wagtail.wagtailcore.blocks.StructBlock([(b'col_one_offset', nicpages.models.ColOffsetChoiceBlock()), (b'col_two_offset', nicpages.models.ColOffsetChoiceBlock()), (b'left_column', wagtail.wagtailcore.blocks.StreamBlock([('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('embedded_video', wagtail.wagtailembeds.blocks.EmbedBlock()), ('google_map', wagtail.wagtailcore.blocks.StructBlock([(b'title', wagtail.wagtailcore.blocks.CharBlock(max_length=255, required=True)), (b'street', wagtail.wagtailcore.blocks.CharBlock(max_length=255, required=True)), (b'postcode', wagtail.wagtailcore.blocks.CharBlock(max_length=255, required=True)), (b'city', wagtail.wagtailcore.blocks.CharBlock(max_length=255, required=True)), (b'map_long', wagtail.wagtailcore.blocks.CharBlock(max_length=255, required=True)), (b'map_lat', wagtail.wagtailcore.blocks.CharBlock(max_length=255, required=True)), (b'map_zoom_level', wagtail.wagtailcore.blocks.CharBlock(default=14, max_length=3, required=True)), (b'width', wagtail.wagtailcore.blocks.IntegerBlock(required=True)), (b'height', wagtail.wagtailcore.blocks.IntegerBlock(required=True))]))], icon='arrow-left', label='Left column content')), (b'right_column', wagtail.wagtailcore.blocks.StreamBlock([('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('embedded_video', wagtail.wagtailembeds.blocks.EmbedBlock()), ('google_map', wagtail.wagtailcore.blocks.StructBlock([(b'title', wagtail.wagtailcore.blocks.CharBlock(max_length=255, required=True)), (b'street', wagtail.wagtailcore.blocks.CharBlock(max_length=255, required=True)), (b'postcode', wagtail.wagtailcore.blocks.CharBlock(max_length=255, required=True)), (b'city', wagtail.wagtailcore.blocks.CharBlock(max_length=255, required=True)), (b'map_long', wagtail.wagtailcore.blocks.CharBlock(max_length=255, required=True)), (b'map_lat', wagtail.wagtailcore.blocks.CharBlock(max_length=255, required=True)), (b'map_zoom_level', wagtail.wagtailcore.blocks.CharBlock(default=14, max_length=3, required=True)), (b'width', wagtail.wagtailcore.blocks.IntegerBlock(required=True)), (b'height', wagtail.wagtailcore.blocks.IntegerBlock(required=True))]))], icon='arrow-right', label='Right column content'))])), ('image_gallery', wagtail.wagtailcore.blocks.StreamBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock()), (b'caption', wagtail.wagtailcore.blocks.CharBlock())])), ('table', wagtail.contrib.table_block.blocks.TableBlock())], blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]