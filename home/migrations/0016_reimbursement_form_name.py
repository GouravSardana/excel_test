# Generated by Django 2.1.3 on 2019-01-06 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_auto_20190105_0918'),
    ]

    operations = [
        migrations.AddField(
            model_name='reimbursement_form',
            name='name',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
