# Generated by Django 4.0.4 on 2022-05-21 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0005_rename_categoria_livro_categoria_id_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="livro",
            old_name="categoria_id",
            new_name="categoria",
        ),
        migrations.RenameField(
            model_name="livro",
            old_name="editora_id",
            new_name="editora",
        ),
    ]
