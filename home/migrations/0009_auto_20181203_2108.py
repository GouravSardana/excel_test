# Generated by Django 2.1.3 on 2018-12-03 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20181203_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budget_approval',
            name='id',
            field=models.CharField(max_length=30, primary_key=True, serialize=False),
        ),
    ]
