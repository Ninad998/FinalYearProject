# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-21 07:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_id', models.IntegerField()),
                ('authorList', models.CharField(max_length=200)),
                ('test_acc', models.DecimalField(decimal_places=10, max_digits=11, null=True)),
                ('test_bin', models.DecimalField(decimal_places=1, max_digits=2, null=True)),
                ('upload_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('completed', models.DecimalField(decimal_places=1, default=0.0, max_digits=2)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]