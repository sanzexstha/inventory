# Generated by Django 3.0 on 2020-02-20 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0004_auto_20200220_0655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='is_accepted',
            field=models.BooleanField(null=True),
        ),
    ]