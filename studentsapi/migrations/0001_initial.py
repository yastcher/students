# Generated by Django 3.1.5 on 2021-01-22 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=100)),
                ('birthdate', models.DateField(default='1900-01-01', null=True)),
                ('record_status', models.CharField(choices=[('2', 'неуд'), ('3', 'уд'), ('4', 'хор'), ('5', 'отл')], default='неуд', max_length=4)),
            ],
        ),
    ]
