# Generated by Django 4.2.6 on 2023-10-18 19:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_filme_categorias'),
    ]

    operations = [
        migrations.CreateModel(
            name='Atuacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('personagem', models.CharField(max_length=100)),
                ('filme', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.filme')),
                ('membro', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.membro')),
                ('tipo_atuacao', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.tipoatuacao')),
            ],
        ),
    ]