# Generated by Django 4.2.4 on 2024-11-09 16:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AstronomyBlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(validators=[django.core.validators.RegexValidator('^[a-zA-Z0-9_-]+$', 'only letters, numbers, hyphens and underscores')])),
                ('body', models.TextField()),
                ('category', models.IntegerField(choices=[(0, 'Interesting Fact'), (1, 'Upcoming Event'), (2, 'Mathematical')])),
            ],
            options={
                'db_table': 'blog_posts',
            },
        ),
    ]