# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-03 10:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, max_length=512)),
                ('description', models.CharField(blank=True, max_length=32)),
                ('resume', models.CharField(blank=True, max_length=32)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=128)),
                ('url', models.CharField(blank=True, max_length=256)),
                ('badge', models.CharField(blank=True, max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='CourseStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='ProviderProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username_provider', models.CharField(blank=True, max_length=30)),
                ('courses', models.ManyToManyField(through='core.CourseStatus', to='core.Course')),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Provider')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('c', 'completed'), ('i', 'in_progress')], max_length=1)),
            ],
        ),
        migrations.AddField(
            model_name='coursestatus',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.ProviderProfile'),
        ),
        migrations.AddField(
            model_name='coursestatus',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Status'),
        ),
        migrations.AddField(
            model_name='course',
            name='provider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Provider'),
        ),
    ]