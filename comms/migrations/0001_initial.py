# Generated by Django 3.0.4 on 2020-04-23 14:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(max_length=50, verbose_name='What is the name of your business?')),
                ('website', models.CharField(choices=[('Landing page/Brochure website', 'Landing page/Brochure website'), ('Multipaged information website', 'Multipaged information website'), ('Ecommerce/Webstore', 'Ecommerce/Webstore'), ('Something Else', 'Something Else')], max_length=50, verbose_name='What kind of website would you like?')),
                ('functionality', models.CharField(max_length=200, verbose_name='What functionality would you like your website to have?')),
                ('url', models.CharField(max_length=200, verbose_name='If you already have a website please add the URL here')),
                ('business_type', models.CharField(max_length=200, verbose_name='What does your business do?')),
                ('customer', models.CharField(max_length=200, verbose_name='Who are your main customers/clients?')),
                ('message', models.CharField(max_length=200, verbose_name='Please provide any extra information that you think might be useful')),
                ('client', models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
