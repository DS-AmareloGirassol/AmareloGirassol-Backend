# Generated by Django 4.2.1 on 2024-06-30 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0003_person_semester_being_attended'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='description',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
