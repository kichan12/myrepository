# Generated by Django 4.0.6 on 2022-08-10 13:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('petpe', '0004_alter_story_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='image_likes',
            field=models.ManyToManyField(blank=True, related_name='post_image_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
