from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class order(models.Model):
    WEBSITE_CHOICES = (
        ('Landing page/Brochure website', 'Landing page/Brochure website'),
        ('Multipaged information website',
         'Multipaged information website'),
        ('Ecommerce/Webstore', 'Ecommerce/Webstore'),
        ('Something Else', 'Something Else')
    )
    FUNCTIONALITY_CHOICES = (
        ('Online Payments', 'Online Payments'),
        ('Shopping Cart/Checkout', 'Shopping Cart/Checkout'),
        ('User Registration & Login', 'User Registration & Login'),
        ('Something Else', 'Something Else')
    )
    business_name = models.CharField("What is the name of your business?", max_length=50)
    website = models.CharField(
        "What kind of website would you like?", max_length=50, choices=WEBSITE_CHOICES)
    functionality = models.CharField(
        "What functionality would you like your website to have?", max_length=50, choices=FUNCTIONALITY_CHOICES)
    url = models.CharField(
        "If you already have a website please add the URL here", max_length=200)
    business_type = models.CharField("What does your business do?", max_length=200)
    customer = models.CharField(
        "Who are your main customers/clients?", max_length=200)
    message = models.CharField(
        "Please provide any extra information that you think might be useful", max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
