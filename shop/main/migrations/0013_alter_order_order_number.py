# Generated by Django 3.2.5 on 2021-07-19 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20210719_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_number',
            field=models.IntegerField(default=0, unique=True),
        ),
    ]
