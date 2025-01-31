# Generated by Django 4.2.13 on 2024-05-12 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('comments', models.CharField(blank=True, max_length=400, null=True)),
                ('status', models.CharField(max_length=100)),
                ('created', models.DateField(auto_now_add=True)),
                ('modified', models.DateField(auto_now=True)),
            ],
        ),
    ]