# Generated by Django 4.0.2 on 2022-02-23 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fifthapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
