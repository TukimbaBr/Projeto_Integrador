# Generated by Django 4.0.4 on 2024-04-07 07:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ficha_paciente', '0004_idoso_slug_alter_idoso_id_idoso'),
    ]

    operations = [
        migrations.RenameField(
            model_name='idoso',
            old_name='slug',
            new_name='slug_idoso',
        ),
    ]
