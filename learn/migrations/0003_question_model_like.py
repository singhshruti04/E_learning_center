# Generated by Django 3.0.6 on 2020-08-01 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0002_auto_20200731_1051'),
    ]

    operations = [
        migrations.AddField(
            model_name='question_model',
            name='like',
            field=models.IntegerField(default='0'),
            preserve_default=False,
        ),
    ]
