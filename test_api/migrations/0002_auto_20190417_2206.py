# Generated by Django 2.2 on 2019-04-17 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='is_activated',
            new_name='is_active',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='is_stuff',
            field=models.BooleanField(default=False),
        ),
    ]
