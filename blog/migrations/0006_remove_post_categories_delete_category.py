# Generated by Django 4.2.16 on 2024-12-06 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_category_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='categories',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
