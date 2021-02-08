# Generated by Django 3.0.4 on 2020-03-17 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('image', '0003_delete_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cid', models.IntegerField(max_length=10)),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
                ('mobile', models.IntegerField(max_length=10)),
                ('prize', models.IntegerField(max_length=10)),
                ('hotel_Main_Img', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
