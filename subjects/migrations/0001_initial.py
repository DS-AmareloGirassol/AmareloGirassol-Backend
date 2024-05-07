# Generated by Django 4.1 on 2024-05-02 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Nome da Matéria', max_length=50)),
                ('code', models.CharField(help_text='Código da Disciplina', max_length=10)),
            ],
        ),
    ]