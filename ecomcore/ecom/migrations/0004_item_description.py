# Generated by Django 2.2.5 on 2019-09-11 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0003_item_discount_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.TextField(default='This is a test description'),
            preserve_default=False,
        ),
    ]
