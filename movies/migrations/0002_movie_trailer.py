# Generated by Django 5.1.3 on 2024-11-29 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="movie",
            name="trailer",
            field=models.CharField(
                blank=True, help_text="YouTube video ID for the trailer", max_length=100
            ),
        ),
    ]