# Generated by Django 3.0.4 on 2020-05-07 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_auto_20200507_1507'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='last4',
            field=models.CharField(default=0, max_length=4),
            preserve_default=False,
        ),
    ]
