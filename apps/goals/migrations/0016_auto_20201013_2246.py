# Generated by Django 2.2.16 on 2020-10-13 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0015_goal_progress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='weight',
            field=models.PositiveSmallIntegerField(default=1),
        ),
    ]