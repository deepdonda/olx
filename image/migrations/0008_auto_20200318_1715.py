# Generated by Django 3.0.4 on 2020-03-18 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0007_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='mobile',
            field=models.IntegerField(max_length=11),
        ),
    ]
