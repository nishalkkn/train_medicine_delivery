# Generated by Django 3.2.21 on 2024-01-15 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('payment_id', models.AutoField(primary_key=True, serialize=False)),
                ('account_name', models.CharField(db_column='account name', max_length=25)),
                ('account_no', models.IntegerField(db_column='account no')),
                ('cvv', models.CharField(max_length=25)),
                ('amount', models.IntegerField()),
                ('time', models.TimeField()),
                ('date', models.DateField()),
            ],
            options={
                'db_table': 'payment',
                'managed': False,
            },
        ),
    ]
