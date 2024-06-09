# Generated by Django 4.1 on 2024-05-18 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Nome do Post', max_length=50)),
                ('description', models.CharField(help_text='Descricao do Post', max_length=500)),
                ('link', models.URLField(max_length=100)),
            ],
        ),
    ]
