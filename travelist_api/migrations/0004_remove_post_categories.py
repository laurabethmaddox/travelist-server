# Generated by Django 4.0.4 on 2022-06-10 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travelist_api', '0003_post_categories'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='categories',
        ),
    ]