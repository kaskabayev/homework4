# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('author', models.CharField(max_length=1000)),
                ('text', models.CharField(max_length=1000)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('author', models.CharField(max_length=1000)),
                ('title', models.CharField(max_length=1000)),
                ('text', models.CharField(max_length=1000)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('upd_date', models.DateTimeField(auto_now=True)),
                ('is_public', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(to='question.Post'),
            preserve_default=True,
        ),
    ]
