# Generated by Django 4.0.2 on 2022-02-21 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_connection_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='krmap',
            name='id',
        ),
        migrations.AlterField(
            model_name='krmap',
            name='identifier',
            field=models.CharField(max_length=70, primary_key=True, serialize=False),
        ),
    ]
