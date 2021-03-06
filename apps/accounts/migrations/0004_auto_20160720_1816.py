# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-20 18:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20160713_1730'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='password_reset_answer_1',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='password_reset_answer_2',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='password_reset_answer_3',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='password_reset_question_1',
            field=models.CharField(choices=[('1', 'What is your favorite color?'), ('2', 'What is your favorite vegetable?'), ('3', 'What is your favorite movie?')], default='1', max_length=1),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='password_reset_question_2',
            field=models.CharField(choices=[('1', 'What was the make of your first automobile?'), ('2', "What was your maternal grandmother's maiden name?"), ('3', "What was your paternal grandmother's maiden name?")], default='1', max_length=1),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='password_reset_question_3',
            field=models.CharField(choices=[('1', 'What was the make of your first automobile?'), ('2', "What was your maternal grandmother's maiden name?"), ('3', "What was your paternal grandmother's maiden name?")], default='1', max_length=1),
        ),
    ]
