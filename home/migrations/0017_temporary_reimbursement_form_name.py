# Generated by Django 2.1.3 on 2019-01-06 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_reimbursement_form_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='temporary_reimbursement_form',
            name='name',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
