# Generated by Django 2.1.15 on 2020-05-27 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20200527_1735'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('username', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=250)),
                ('firstname', models.CharField(max_length=250)),
                ('lastname', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=250)),
                ('city', models.CharField(max_length=250)),
                ('country', models.CharField(max_length=250)),
                ('postalcode', models.CharField(max_length=250)),
                ('mobile', models.CharField(max_length=250)),
                ('dateofbirth', models.DateField()),
                ('aadhar_number', models.CharField(max_length=250)),
            ],
        ),
    ]