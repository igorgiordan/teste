# Generated by Django 2.1 on 2018-09-12 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mercadolivre', '0004_remove_produto_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='ofertamax',
        ),
    ]
