# Generated by Django 4.0.3 on 2022-05-05 13:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000000)),
                ('create_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
