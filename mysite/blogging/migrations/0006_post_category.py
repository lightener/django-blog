# Generated by Django 2.1.5 on 2022-05-16 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogging', '0005_auto_20220515_1814'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(blank=True, related_name='categories', to='blogging.Category'),
        ),
    ]