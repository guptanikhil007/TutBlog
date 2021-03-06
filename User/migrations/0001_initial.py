# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-20 10:57
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
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('email_confirmed', models.BooleanField(default=False)),
                ('contribution', models.IntegerField(default=0)),
                ('organization', models.CharField(blank=True, max_length=200, null=True)),
                ('facebook_url', models.URLField(blank=True, null=True)),
                ('city', models.CharField(blank=True, max_length=200, null=True)),
                ('country', models.CharField(blank=True, max_length=200, null=True)),
                ('googleplus', models.URLField(blank=True, null=True)),
                ('mobile', models.BigIntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(1, 'Following'), (2, 'Blocked')])),
                ('from_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_people', to='User.Profile')),
                ('to_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_people', to='User.Profile')),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='relationships',
            field=models.ManyToManyField(related_name='related_to', through='User.Relationship', to='User.Profile'),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
