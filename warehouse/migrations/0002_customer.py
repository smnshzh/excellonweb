# Generated by Django 3.0.5 on 2020-08-21 18:25

from django.db import migrations, models


class Migration (migrations.Migration):
    dependencies = [
        ('warehouse', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel (
            name='Customer',
            fields=[
                ('id', models.AutoField (auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.PositiveIntegerField ( )),
                ('name', models.CharField (max_length=35)),
                ('tel', models.CharField (max_length=35)),
                ('address', models.CharField (max_length=1000)),
            ],
        ),
    ]
