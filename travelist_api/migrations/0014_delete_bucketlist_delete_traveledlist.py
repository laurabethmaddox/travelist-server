# Generated by Django 4.0.4 on 2022-06-20 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travelist_api', '0013_alter_post_img'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BucketList',
        ),
        migrations.DeleteModel(
            name='TraveledList',
        ),
    ]
