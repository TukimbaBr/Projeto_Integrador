# Generated by Django 4.0.4 on 2024-03-31 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ficha_paciente', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idoso',
            name='cidade_idoso',
            field=models.CharField(max_length=55),
        ),
    ]
