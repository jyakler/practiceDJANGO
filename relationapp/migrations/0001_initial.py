# Generated by Django 4.0.2 on 2022-02-23 00:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('deptid', models.IntegerField(primary_key=True, serialize=False)),
                ('deptname', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('locationname', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=8)),
                ('addr', models.CharField(max_length=20)),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='relationapp.department')),
            ],
        ),
        migrations.AddField(
            model_name='department',
            name='location',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='relationapp.location'),
        ),
    ]
