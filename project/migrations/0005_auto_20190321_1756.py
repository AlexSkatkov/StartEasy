# Generated by Django 2.1 on 2019-03-21 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_auto_20190321_1658'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='user1',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='user2',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='user3',
            field=models.TextField(blank=True),
        ),
    ]