# Generated by Django 3.2.3 on 2021-07-18 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210718_2034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor_reg',
            name='phone_no',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='donorreg',
            name='phone_no',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='hotelreg',
            name='phone_no',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='volreg',
            name='phone_no',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
