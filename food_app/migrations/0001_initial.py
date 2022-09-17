# Generated by Django 3.2 on 2021-06-10 16:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CardGeneration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cardnum', models.CharField(default=0, max_length=10)),
                ('date', models.DateTimeField(auto_now=True, null=True)),
                ('used', models.BooleanField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='UsedCards',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now=True)),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food_app.cardgeneration')),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.hotelreg')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(max_length=30, null=True)),
                ('date', models.DateField(auto_now=True, null=True)),
                ('time', models.TimeField(auto_now=True, null=True)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.hotelreg')),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=1000, null=True)),
                ('reply', models.CharField(max_length=1000, null=True)),
                ('date', models.DateTimeField(auto_now=True)),
                ('donor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.donorreg')),
                ('hotel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.hotelreg')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.usertype')),
                ('volunteer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.volreg')),
            ],
        ),
        migrations.CreateModel(
            name='DonationReg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donation', models.IntegerField(null=True)),
                ('time', models.TimeField(auto_now=True)),
                ('date', models.DateField(auto_now=True)),
                ('details', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.donorreg')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CardRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('photo', models.ImageField(null=True, upload_to='', verbose_name='images/')),
                ('address', models.CharField(max_length=50)),
                ('aadhar', models.CharField(max_length=40, null=True)),
                ('date', models.DateTimeField(auto_now=True, null=True)),
                ('approved', models.BooleanField(default=0, null=True)),
                ('rejected', models.BooleanField(default=0, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('volun', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.volreg')),
            ],
        ),
        migrations.AddField(
            model_name='cardgeneration',
            name='card',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food_app.cardregistration'),
        ),
    ]
