# Generated by Django 5.0.7 on 2024-07-24 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_alter_media_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='category',
            field=models.CharField(choices=[('Recommended', 'Recommended'), ('Live Show', 'Live Shows')], max_length=20),
        ),
    ]
