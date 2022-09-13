# Generated by Django 4.1 on 2022-09-13 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DatosFamilia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('apellido', models.CharField(max_length=60)),
                ('dni', models.IntegerField()),
                ('genero', models.CharField(max_length=60)),
                ('profesion', models.CharField(max_length=60)),
                ('correo', models.EmailField(max_length=254)),
            ],
        ),
    ]