# Generated by Django 2.2.6 on 2020-01-22 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0002_chamado_data_inicio'),
    ]

    operations = [
        migrations.AddField(
            model_name='chamado',
            name='data_fim',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]