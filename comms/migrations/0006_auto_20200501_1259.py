# Generated by Django 3.0.4 on 2020-05-01 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comms', '0005_auto_20200427_1401'),
    ]

    operations = [
        migrations.CreateModel(
            name='question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('question', models.CharField(max_length=3000)),
                ('Answer', models.CharField(max_length=3000)),
            ],
        ),
        migrations.AlterField(
            model_name='order',
            name='url',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='If you already have a website please add the URL here'),
        ),
    ]
