# Generated by Django 3.0.4 on 2020-04-27 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comms', '0004_auto_20200427_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='business_type',
            field=models.CharField(max_length=2000, verbose_name='What does your business do?'),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.CharField(max_length=2000, verbose_name='Who are your main customers/clients?'),
        ),
        migrations.AlterField(
            model_name='order',
            name='functionality',
            field=models.CharField(max_length=1000, verbose_name='What would you like users to do on your website?'),
        ),
        migrations.AlterField(
            model_name='order',
            name='message',
            field=models.CharField(max_length=3000, verbose_name='Please provide any extra information that you think might be useful'),
        ),
    ]