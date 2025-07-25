# Generated by Django 5.2.4 on 2025-07-22 11:41

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_movie_avarage_rating'),
        ('ratings', '0002_alter_rating_unique_together'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='rating',
            unique_together={('user', 'movie')},
        ),
    ]
