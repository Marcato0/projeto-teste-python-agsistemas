# Generated by Django 4.0.4 on 2022-06-02 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locadora', '0004_remove_controle_create_at_remove_controle_update_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='controle',
            name='data_retorno',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='controle',
            name='data_saida',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='controle',
            name='hora_retorno',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='controle',
            name='hora_saida',
            field=models.CharField(max_length=255),
        ),
    ]
