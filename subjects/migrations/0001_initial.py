# Generated by Django 4.1 on 2024-06-28 13:22

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
                ('name', models.CharField(help_text='Nome da Matéria', max_length=40)),
                ('code', models.CharField(help_text='Código da Disciplina', max_length=10, unique=True)),
                ('workload', models.IntegerField()),
                ('default_semester', models.IntegerField()),
            ],
        ),
    ]
