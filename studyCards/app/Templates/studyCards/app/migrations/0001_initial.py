# Generated by Django 4.2.6 on 2023-10-26 10:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_disciplina', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Conteudo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_conteudo', models.CharField(max_length=50)),
                ('descricao_conteudo', models.TextField()),
                ('disciplina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.disciplina')),
            ],
        ),
        migrations.CreateModel(
            name='Cartao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('termo', models.CharField(max_length=100)),
                ('definicao', models.TextField()),
                ('conteudo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.conteudo')),
            ],
        ),
    ]