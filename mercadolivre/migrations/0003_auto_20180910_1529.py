# Generated by Django 2.1 on 2018-09-10 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mercadolivre', '0002_auto_20180910_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='descricao',
            field=models.TextField(verbose_name='Descrição'),
        ),
    ]
