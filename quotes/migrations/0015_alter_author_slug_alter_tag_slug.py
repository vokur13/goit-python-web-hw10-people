# Generated by Django 4.2.4 on 2023-09-05 18:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("quotes", "0014_alter_author_slug_alter_tag_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="author",
            name="slug",
            field=models.SlugField(unique=True),
        ),
        migrations.AlterField(
            model_name="tag",
            name="slug",
            field=models.SlugField(unique=True),
        ),
    ]