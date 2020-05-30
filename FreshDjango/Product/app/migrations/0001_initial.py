# Generated by Django 3.0.6 on 2020-05-29 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegisterUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=20, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('hashedPassword', models.CharField(max_length=256)),
            ],
        ),
    ]