# Generated by Django 3.0.3 on 2020-02-20 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Avc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lineno', models.IntegerField()),
                ('noo', models.FloatField()),
                ('workdays', models.FloatField()),
                ('dwh', models.FloatField()),
                ('absent', models.FloatField()),
                ('efficiency', models.FloatField()),
                ('mac', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Cpr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderno', models.IntegerField()),
                ('ltlc', models.IntegerField()),
                ('orderqty', models.IntegerField()),
                ('smv', models.IntegerField()),
                ('crm', models.FloatField()),
                ('capd', models.FloatField()),
                ('crd', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Mat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderno', models.IntegerField()),
                ('fin', models.CharField(max_length=2)),
                ('threads', models.CharField(max_length=2)),
                ('sewtrim', models.CharField(max_length=2)),
                ('fintrim', models.CharField(max_length=2)),
                ('packtrim', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Ord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderno', models.IntegerField()),
                ('styleno', models.IntegerField()),
                ('orderqty', models.IntegerField()),
                ('ordercd', models.DateField()),
                ('plancd', models.DateField()),
                ('ocd', models.DateField()),
                ('ltf', models.IntegerField()),
                ('ltb', models.IntegerField()),
            ],
        ),
    ]
