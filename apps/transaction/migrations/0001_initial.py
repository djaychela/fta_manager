# Generated by Django 3.1 on 2020-08-21 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client', '0003_auto_20200821_0818'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lender', models.CharField(max_length=80)),
                ('submitted', models.BooleanField()),
                ('eid', models.BooleanField()),
                ('ff360', models.BooleanField()),
                ('docs', models.BooleanField()),
                ('rwl', models.BooleanField()),
                ('file1_30', models.BooleanField()),
                ('val_date', models.DateTimeField()),
                ('offer_date', models.DateTimeField()),
                ('fee', models.IntegerField()),
                ('fee_paid', models.BooleanField()),
                ('completion', models.DateTimeField()),
                ('comm_recd', models.DateTimeField()),
                ('review_date', models.DateTimeField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.client')),
            ],
        ),
    ]