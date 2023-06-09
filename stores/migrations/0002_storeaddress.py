# Generated by Django 4.2.1 on 2023-05-09 23:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StoreAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField(max_length=25)),
                ('longitude', models.FloatField(max_length=25)),
                ('address', models.CharField(max_length=255)),
                ('neighborhood', models.CharField(max_length=255)),
                ('post_code', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('complement', models.CharField(max_length=255)),
                ('store_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='stores.store', verbose_name='store_address')),
            ],
        ),
    ]
