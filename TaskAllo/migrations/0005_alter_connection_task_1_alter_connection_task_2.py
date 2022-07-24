# Generated by Django 4.0.6 on 2022-07-24 21:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TaskAllo', '0004_remove_connection_team_1_remove_connection_team_2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connection',
            name='task_1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='task_1', to='TaskAllo.task'),
        ),
        migrations.AlterField(
            model_name='connection',
            name='task_2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='task_2', to='TaskAllo.task'),
        ),
    ]
