# Generated by Django 3.0.4 on 2020-04-13 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('signalData', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(default='xxxxxxxx', max_length=100)),
                ('username', models.CharField(default='Anonymous', max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('coordinates', models.ManyToManyField(to='signalData.Coordinate')),
            ],
            options={
                'verbose_name': 'Uset',
                'verbose_name_plural': 'Users',
                'ordering': ('id',),
            },
        ),
    ]