# Generated by Django 4.2.6 on 2023-10-18 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_pais'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pais',
            options={'verbose_name_plural': 'Países'},
        ),
        migrations.AlterModelOptions(
            name='tipoatuacao',
            options={'verbose_name_plural': 'Tipos de Atuacao'},
        ),
        migrations.RenameField(
            model_name='pais',
            old_name='descricao',
            new_name='nome',
        ),
    ]