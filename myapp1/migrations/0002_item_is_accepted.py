# Generated by Django 3.0 on 2020-02-20 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='is_accepted',
            field=models.BooleanField(default=True),
        ),
    ]
