# Generated by Django 3.2.9 on 2021-12-09 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('cost', models.CharField(max_length=50)),
                ('details', models.CharField(max_length=500)),
            ],
        ),
    ]
