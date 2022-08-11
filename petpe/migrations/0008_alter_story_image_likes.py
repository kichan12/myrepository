# Generated by Django 4.0.6 on 2022-08-11 13:14

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('petpe', '0007_merge_0005_story_image_likes_0006_delete_mystory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='image_likes',
            field=models.ManyToManyField(blank=True, related_name='story_image_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
