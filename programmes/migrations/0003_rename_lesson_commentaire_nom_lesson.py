# Generated by Django 3.2.8 on 2021-11-19 03:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('programmes', '0002_commentaire_reponse'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commentaire',
            old_name='lesson',
            new_name='nom_lesson',
        ),
    ]