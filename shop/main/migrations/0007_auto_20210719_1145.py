# Generated by Django 3.2.5 on 2021-07-19 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_cartelement_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='cart_element',
        ),
        migrations.AddField(
            model_name='cart',
            name='cart_element',
            field=models.ManyToManyField(to='main.CartElement'),
        ),
    ]
