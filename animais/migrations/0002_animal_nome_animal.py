# Generated by Django 4.0.4 on 2022-05-14 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animais', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='nome_animal',
            field=models.CharField(default='Leão', max_length=100),
            preserve_default=False,
        ),
    ]
