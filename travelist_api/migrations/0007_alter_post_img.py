# Generated by Django 4.0.4 on 2022-06-10 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelist_api', '0006_alter_post_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(upload_to='images'),
        ),
    ]