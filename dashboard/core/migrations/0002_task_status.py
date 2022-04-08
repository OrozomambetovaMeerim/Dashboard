# Generated by Django 4.0.3 on 2022-04-08 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.IntegerField(choices=[(1, 'To Do'), (2, 'On Progress'), (3, 'Done')], default=1),
        ),
    ]