# Generated by Django 4.0.2 on 2022-02-21 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_metadata_connection_meta_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connection',
            name='meta_data',
            field=models.JSONField(),
        ),
        migrations.AlterField(
            model_name='krmap',
            name='is_active',
            field=models.BooleanField(),
        ),
    ]
