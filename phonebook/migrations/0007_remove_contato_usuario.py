# Generated by Django 4.1.5 on 2023-01-14 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phonebook', '0006_contato_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contato',
            name='usuario',
        ),
    ]
