# Generated by Django 5.1 on 2024-11-28 08:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blogapp", "0002_categories_delete_catagories"),
        ("textwriter", "0003_alter_textwriter_body"),
    ]

    operations = [
        migrations.AlterField(
            model_name="textwriter",
            name="Book_category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="blogapp.categories"
            ),
        ),
    ]