# Generated by Django 2.1.3 on 2018-11-29 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='n',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='p',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
