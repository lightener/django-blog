# Generated by Django 2.1.5 on 2022-05-16 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogging', '0004_auto_20220515_1801'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
        migrations.AddField(
            model_name='category',
            name='posts',
            field=models.ManyToManyField(blank=True, related_name='categories', to='blogging.Post'),
        ),
    ]
