# Generated by Django 3.0.4 on 2020-05-07 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0003_invoice_last4'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='card_type',
            field=models.CharField(default='Visa', max_length=20),
            preserve_default=False,
        ),
    ]
