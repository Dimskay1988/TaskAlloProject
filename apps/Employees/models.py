from django.db import models
from django.contrib.auth.models import AbstractUser
from autoslug import AutoSlugField


class RolesChoice(models.TextChoices):
    worker = 'worker'
    manager = 'manager'
    admin = 'admin'


class StatusWorkerChoice(models.TextChoices):
    in_team = 'in_team'
    bench = 'bench'
    fired = 'fired'


class CustomUser(AbstractUser):
    role = models.CharField(choices=RolesChoice.choices, max_length=20)
    status = models.CharField(max_length=15, choices=StatusWorkerChoice.choices, default=StatusWorkerChoice.bench)
    team = models.ForeignKey('Team', on_delete=models.SET_NULL, null=True, related_name="current_team", blank=True)
    slug = AutoSlugField(populate_from='username', unique=True)

    def set_status(self):
        status = {
            True: StatusWorkerChoice.in_team,
            False: StatusWorkerChoice.bench,
        }
        if self.status == StatusWorkerChoice.fired:
            self.team = None
            return
        self.status = status[bool(self.team)]

    @property
    def count_tasks(self):
        return self.assigned_task.count()

    def save(self, *args, **kwargs):
        self.set_status()
        return super().save(*args, **kwargs)


class Team(models.Model):
    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'

    name = models.CharField(max_length=150)
    worker = models.OneToOneField(CustomUser, on_delete=models.SET_NULL, null=True,
                                  limit_choices_to={"role": RolesChoice.worker}, related_name='worker')
    manager = models.ManyToManyField(CustomUser, limit_choices_to={"role": RolesChoice.manager}, related_name='manager')

    def __str__(self):
        return self.name
