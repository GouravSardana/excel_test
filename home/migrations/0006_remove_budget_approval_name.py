# Generated by Django 2.1.3 on 2018-12-03 19:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_budget_approval_request_approval_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='budget_approval',
            name='name',
        ),
    ]
