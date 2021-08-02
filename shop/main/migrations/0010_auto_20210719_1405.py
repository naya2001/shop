# Generated by Django 3.2.5 on 2021-07-19 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_cartelement_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='customer',
        ),
        migrations.AddField(
            model_name='cartelement',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.customer'),
        ),
    ]
