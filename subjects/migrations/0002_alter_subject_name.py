# Generated by Django 4.1 on 2024-05-03 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='name',
            field=models.CharField(help_text='Nome da Matéria', max_length=40),
        ),
    ]
