# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-01-13 06:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0010_course_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='teacher_tell',
            field=models.CharField(default='\u6309\u65f6\u4ea4\u4f5c\u4e1a,\u4e0d\u7136\u53eb\u5bb6\u957f', max_length=300, verbose_name='\u8001\u5e08\u544a\u8bc9\u4f60'),
        ),
        migrations.AddField(
            model_name='course',
            name='you_need_know',
            field=models.CharField(default='\u4e00\u9897\u52e4\u5b66\u7684\u5fc3\u662f\u672c\u8bfe\u7a0b\u5fc5\u8981\u524d\u63d0', max_length=300, verbose_name='\u8bfe\u7a0b\u987b\u77e5'),
        ),
    ]