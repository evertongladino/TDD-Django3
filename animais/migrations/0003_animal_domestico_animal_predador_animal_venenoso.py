# Generated by Django 4.0.4 on 2022-05-14 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animais', '0002_animal_nome_animal'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='domestico',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='animal',
            name='predador',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='animal',
            name='venenoso',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
