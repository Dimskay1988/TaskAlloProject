# Generated by Django 4.0.6 on 2022-07-24 20:14

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Employee',
                'verbose_name_plural': 'Employees',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='StatusEmployee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=120)),
            ],
            options={
                'verbose_name': 'Status Employee',
                'verbose_name_plural': 'Statuses Employee',
            },
        ),
        migrations.CreateModel(
            name='StatusTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=120)),
            ],
            options={
                'verbose_name': 'Status Task',
                'verbose_name_plural': 'Status Tasks',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
            options={
                'verbose_name': 'Team',
                'verbose_name_plural': 'Teams',
            },
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('employee_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='TaskAllo.employee')),
            ],
            options={
                'verbose_name': 'Manager',
                'verbose_name_plural': 'Managers',
            },
            bases=('TaskAllo.employee',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=120)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('deadline', models.DateTimeField(blank=True, null=True)),
                ('connection', models.ManyToManyField(blank=True, null=True, to='TaskAllo.task')),
                ('status_task', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='status_task', to='TaskAllo.statustask')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task_team', to='TaskAllo.team')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='task_author', to='TaskAllo.manager')),
            ],
            options={
                'verbose_name': 'Task',
                'verbose_name_plural': 'Tasks',
            },
        ),
        migrations.CreateModel(
            name='ImageSource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='source_comment', to='TaskAllo.comment')),
                ('task', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='source_task', to='TaskAllo.comment')),
            ],
            options={
                'verbose_name': 'Image Source',
                'verbose_name_plural': 'Image Sources',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Image')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TaskAllo.imagesource')),
            ],
            options={
                'verbose_name': 'Image',
                'verbose_name_plural': 'Images',
            },
        ),
        migrations.AddField(
            model_name='employee',
            name='status_emp',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TaskAllo.statusemployee'),
        ),
        migrations.AddField(
            model_name='comment',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='TaskAllo.employee'),
        ),
        migrations.AddField(
            model_name='comment',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TaskAllo.task'),
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('manager_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='TaskAllo.manager')),
            ],
            options={
                'verbose_name': 'Admin',
                'verbose_name_plural': 'Admins',
            },
            bases=('TaskAllo.manager',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('employee_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='TaskAllo.employee')),
                ('team', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='worker_team', to='TaskAllo.team')),
            ],
            options={
                'verbose_name': 'Worker',
                'verbose_name_plural': 'Workers',
            },
            bases=('TaskAllo.employee',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Managership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='manship_team', to='TaskAllo.team')),
                ('manager', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='manship_manager', to='TaskAllo.manager')),
            ],
            options={
                'verbose_name': 'Managership',
                'verbose_name_plural': 'Managerships',
            },
        ),
        migrations.AddField(
            model_name='manager',
            name='team',
            field=models.ManyToManyField(related_name='manager_team', through='TaskAllo.Managership', to='TaskAllo.team'),
        ),
    ]
