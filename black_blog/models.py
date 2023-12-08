from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=300)
    category = models.CharField(max_length=250)
    body = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    img = models.ImageField(upload_to='black_blog/', null=True)
    view_count = models.BigIntegerField(default=0)
    is_active = models.BooleanField(default=False)

class CategoryPost(models.Model):
    title = models.CharField(max_length=300)

class Navbar(models.Model):
    name = models.CharField(max_length=20)

class SiteTitle(models.Model):
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=120)

class SocialNetwork(models.Model):
    link = models.CharField(max_length=350)
    icon = models.ImageField(upload_to='icon/')

class Podcast(models.Model):
    link = models.CharField(max_length=320)
    name = models.CharField(max_length=120)

class Intervyu(models.Model):
    link = models.CharField(max_length=320)
    name = models.CharField(max_length=120)