# Generated by Django 2.1.3 on 2018-12-07 06:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_temporarybudgetapproval'),
    ]

    operations = [
        migrations.CreateModel(
            name='Temporary_Purchase_order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase_no', models.CharField(max_length=50)),
                ('date_of_purchase', models.CharField(max_length=50)),
                ('attension', models.CharField(max_length=50)),
                ('contact_person', models.CharField(max_length=50)),
                ('tel', models.CharField(max_length=50)),
                ('ventor', models.CharField(max_length=50)),
                ('delivery_date', models.CharField(max_length=50)),
                ('delivery_purchase', models.CharField(max_length=50)),
                ('no', models.CharField(max_length=50)),
                ('product', models.CharField(max_length=50)),
                ('spec', models.CharField(max_length=50)),
                ('unit', models.CharField(max_length=50)),
                ('quantity', models.CharField(max_length=50)),
                ('unit_price', models.CharField(max_length=50)),
                ('sum', models.CharField(max_length=50)),
                ('remark', models.CharField(max_length=50)),
                ('total', models.CharField(max_length=50)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Person_name')),
            ],
        ),
        migrations.CreateModel(
            name='Temporary_Reimbursement_form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=50)),
                ('item', models.CharField(max_length=50)),
                ('paid', models.CharField(max_length=50)),
                ('payment', models.CharField(max_length=50)),
                ('detail', models.CharField(max_length=50)),
                ('amount', models.CharField(max_length=50)),
                ('remark', models.CharField(max_length=50)),
                ('subtotal', models.CharField(max_length=50)),
                ('total', models.CharField(max_length=50)),
            ],
        ),
    ]
