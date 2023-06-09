# Generated by Django 4.2.1 on 2023-05-10 00:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('stores', '0002_storeaddress'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('0', 'Vegano'), ('1', 'Vegetais'), ('2', 'Carnes'), ('3', 'Lanches'), ('4', 'Creps'), ('5', 'Massas')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('is_available', models.BooleanField(default=False)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.category', verbose_name='products')),
                ('store_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stores.store', verbose_name='products')),
            ],
        ),
    ]
