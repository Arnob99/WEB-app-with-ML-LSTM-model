# Generated by Django 2.2 on 2022-05-18 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment_app', '0004_auto_20220518_1223'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data',
            name='comment_length',
        ),
        migrations.AlterField(
            model_name='data',
            name='predictions',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]