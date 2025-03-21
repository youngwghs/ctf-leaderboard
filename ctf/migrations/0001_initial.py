# Generated by Django 4.0.2 on 2022-02-22 19:21

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='Flag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('secret', models.CharField(max_length=200, unique=True, validators=[django.core.validators.RegexValidator('^[a-zA-Z0-9_]+$', message='Invalid secret!')])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('custom_name', models.CharField(blank=True, max_length=40, validators=[django.core.validators.RegexValidator('^[a-zA-Z0-9_ ,]*$', message='Invalid name!')])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_id', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('flag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ctf.flag')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ctf.participant')),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
        migrations.AddConstraint(
            model_name='submission',
            constraint=models.UniqueConstraint(fields=('flag', 'participant'), name='unique_submission'),
        ),
    ]
