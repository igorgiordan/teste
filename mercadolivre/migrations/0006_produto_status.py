# Generated by Django 2.1 on 2018-09-19 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mercadolivre', '0005_remove_produto_ofertamax'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='status',
            field=models.IntegerField(choices=[(1, 'Ativo'), (2, 'Não ativo')], default=1, verbose_name='tipo'),
        ),
    ]
