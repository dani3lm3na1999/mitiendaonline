# Generated by Django 4.2.5 on 2023-10-01 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('description', models.TextField(max_length=200, null=True, verbose_name='Descripción')),
                ('existencias', models.IntegerField(verbose_name='Existencias')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=18, verbose_name='Precio')),
            ],
        ),
    ]