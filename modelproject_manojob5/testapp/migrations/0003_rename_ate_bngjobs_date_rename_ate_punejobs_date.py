# Generated by Django 4.2.3 on 2023-08-27 17:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_bngjobs_hydjobs_punejobs_delete_jobs'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bngjobs',
            old_name='ate',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='punejobs',
            old_name='ate',
            new_name='date',
        ),
    ]
