# Generated by Django 2.2.8 on 2019-12-21 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0002_auto_20191221_2326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='due_date',
            field=models.DateTimeField(),
        ),
    ]