# Generated by Django 4.0.4 on 2022-05-14 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animais', '0003_animal_domestico_animal_predador_animal_venenoso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='domestico',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name='animal',
            name='predador',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name='animal',
            name='venenoso',
            field=models.CharField(max_length=4),
        ),
    ]
