# Generated by Django 3.0.7 on 2020-06-09 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=50, unique=True)),
                ('nationalid', models.CharField(max_length=14)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=6)),
                ('socialstatus', models.CharField(max_length=8)),
                ('address', models.CharField(max_length=70)),
                ('phone1', models.CharField(max_length=11)),
                ('phone2', models.CharField(max_length=11)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]