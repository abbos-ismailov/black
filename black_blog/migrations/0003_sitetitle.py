# Generated by Django 4.2.6 on 2023-12-06 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('black_blog', '0002_categorypost_socialnetwork_remove_blog_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.CharField(max_length=120)),
            ],
        ),
    ]