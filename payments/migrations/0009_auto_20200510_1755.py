# Generated by Django 3.0.4 on 2020-05-10 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0008_auto_20200510_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='stripe_receipt',
            field=models.CharField(max_length=1000),
        ),
    ]
