# Generated by Django 3.2.6 on 2021-09-27 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataSets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField(default=0)),
                ('work', models.TextField(blank=True, null=True)),
                ('fnlwgt', models.IntegerField(default=0)),
                ('education', models.CharField(blank=True, max_length=500, null=True)),
                ('education_num', models.IntegerField(default=0)),
                ('marital_status', models.CharField(blank=True, max_length=500, null=True)),
                ('occupation', models.CharField(blank=True, max_length=500, null=True)),
                ('relationship', models.CharField(blank=True, max_length=50, null=True)),
                ('race', models.CharField(blank=True, max_length=100, null=True)),
                ('sex', models.CharField(blank=True, max_length=10, null=True)),
                ('capital_gain', models.IntegerField(default=0)),
                ('capital_loss', models.IntegerField(default=0)),
                ('hours_per_week', models.IntegerField(default=0)),
                ('native_country', models.CharField(blank=True, max_length=100, null=True)),
                ('salary', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
