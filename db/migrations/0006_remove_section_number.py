# Generated by Django 3.0.1 on 2019-12-24 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0005_remove_section_subsection'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='section',
            name='number',
        ),
    ]