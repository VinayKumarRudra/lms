# Generated by Django 2.1.15 on 2020-05-28 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher_Class',
            fields=[
                ('std', models.CharField(max_length=250)),
                ('section', models.CharField(max_length=250)),
                ('subcode', models.CharField(max_length=250)),
                ('staffid', models.CharField(max_length=250)),
                ('markid', models.CharField(max_length=250, primary_key=True, serialize=False)),
                ('sesid', models.CharField(max_length=250)),
                ('sesno', models.IntegerField()),
            ],
        ),
    ]
