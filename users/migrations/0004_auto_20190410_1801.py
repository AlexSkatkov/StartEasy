# Generated by Django 2.1 on 2019-04-10 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20190410_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='avatar.png', upload_to='pic_folder'),
        ),
    ]
