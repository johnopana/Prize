# Generated by Django 3.1.4 on 2021-06-04 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_tags'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tags',
            new_name='Tag',
        ),
    ]
