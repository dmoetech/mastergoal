# Generated by Django 2.2.16 on 2021-02-22 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20210222_1427'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='page_choice',
        ),
    ]