# Generated by Django 4.0.4 on 2022-05-21 07:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="livro",
            old_name="isbn",
            new_name="ISBN",
        ),
    ]
