# Generated by Django 2.1.3 on 2018-12-03 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20181129_2103'),
    ]

    operations = [
        migrations.AddField(
            model_name='budget_approval',
            name='request_approval_date',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]