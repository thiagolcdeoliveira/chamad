# Generated by Django 2.2.6 on 2020-01-24 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0007_auto_20200124_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chamado',
            name='cod',
            field=models.CharField(max_length=200, verbose_name='Codigo do Chamado'),
        ),
    ]