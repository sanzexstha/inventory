# Generated by Django 3.0 on 2020-02-19 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemrequest',
            name='item',
        ),
        migrations.AddField(
            model_name='itemrequest',
            name='item',
            field=models.ManyToManyField(related_name='item_request', to='myapp.Item'),
        ),
    ]
