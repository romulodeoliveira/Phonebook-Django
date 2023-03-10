# Generated by Django 4.1.5 on 2023-01-07 21:36

from django.db import migrations, models
import phonebook.models


class Migration(migrations.Migration):

    dependencies = [
        ('phonebook', '0003_alter_contato_telefone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='telefone',
            field=models.CharField(max_length=11, validators=[phonebook.models.validar_numero], verbose_name='Número | Ex.: 85912345678'),
        ),
    ]
