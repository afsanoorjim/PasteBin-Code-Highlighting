# Generated by Django 5.1 on 2024-08-10 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Snippets", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="snippets",
            name="code",
            field=models.TextField(default="you code"),
        ),
    ]
