# Generated by Django 4.2.1 on 2023-05-09 22:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_usertype_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='users', to='accounts.usertype'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usertype',
            name='name',
            field=models.CharField(choices=[('0', 'owner'), ('1', 'user')], max_length=1),
        ),
    ]
