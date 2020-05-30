# Generated by Django 2.1.15 on 2020-05-28 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('studid', models.CharField(max_length=250, primary_key=True, serialize=False)),
                ('studname', models.CharField(max_length=100)),
                ('std', models.CharField(max_length=250)),
                ('section', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=250)),
                ('mobile', models.CharField(max_length=250)),
                ('sesid', models.CharField(max_length=250)),
                ('sesno', models.IntegerField()),
            ],
        ),
    ]