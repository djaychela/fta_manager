# Generated by Django 3.1 on 2020-08-21 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0002_auto_20200821_0902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='lender',
            field=models.CharField(blank=True, max_length=80),
        ),
    ]