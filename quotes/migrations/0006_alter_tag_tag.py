# Generated by Django 4.2.4 on 2023-09-04 13:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("quotes", "0005_remove_tag_tag"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tag",
            name="tag",
            field=models.CharField(max_length=64, unique=True),
        ),
    ]
