# Generated by Django 5.0.7 on 2024-07-24 03:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('release_year', models.DateField()),
                ('genre', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('poster', models.ImageField(upload_to='media_posters/')),
                ('rating', models.DecimalField(decimal_places=1, max_digits=2)),
                ('movie_theater', models.CharField(max_length=100)),
                ('ticket_price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('language', models.CharField(max_length=250)),
                ('duration', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('Recommended', 'Recommended'), ('Upcoming', 'Upcoming'), ('Live', 'Live'), ('Show Recommended', 'Show Recommended'), ('Show Upcoming', 'Show Upcoming'), ('Show Live', 'Show Live')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_text', models.TextField()),
                ('reviewer', models.CharField(max_length=100)),
                ('rating', models.DecimalField(decimal_places=1, max_digits=2)),
                ('media', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='movies.media')),
            ],
        ),
    ]
