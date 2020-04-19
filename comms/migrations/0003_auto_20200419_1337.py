# Generated by Django 3.0.4 on 2020-04-19 13:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('comms', '0002_remove_query_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('website', models.CharField(choices=[('Landing page/Brochure website', 'Landing page/Brochure website'), ('Multipaged information website', 'Multipaged information website'), ('Ecommerce/Webstore', 'Ecommerce/Webstore'), ('Something Else', 'Something Else')], max_length=50, verbose_name='What kind of website would you like?')),
                ('functionality', models.CharField(choices=[('Online Payments', 'Online Payments'), ('Shopping Cart/Checkout', 'Shopping Cart/Checkout'), ('User Registration & Login', 'User Registration & Login'), ('Something Else', 'Something Else')], max_length=50, verbose_name='What functionality would you like your website to have?')),
                ('url', models.CharField(max_length=200, verbose_name='If you already have a website please add the URL here')),
                ('business', models.CharField(max_length=200, verbose_name='What does your business do?')),
                ('customer', models.CharField(max_length=200, verbose_name='Who are your main customers/clients?')),
                ('message', models.CharField(max_length=200, verbose_name='Please provide any extra information that you think might be useful')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='query',
        ),
    ]
