# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class User(models.Model):

    #__User_FIELDS__
    id = models.IntegerField(null=True, blank=True)
    name = models.TextField(max_length=255, null=True, blank=True)
    dep_id = models.ForeignKey(department, on_delete=models.CASCADE)
    email = models.TextField(max_length=255, null=True, blank=True)
    group_id = models.ForeignKey(groups, on_delete=models.CASCADE)

    #__User_FIELDS__END

    class Meta:
        verbose_name        = _("User")
        verbose_name_plural = _("User")


class Department(models.Model):

    #__Department_FIELDS__
    id = models.IntegerField(null=True, blank=True)
    name = models.TextField(max_length=255, null=True, blank=True)

    #__Department_FIELDS__END

    class Meta:
        verbose_name        = _("Department")
        verbose_name_plural = _("Department")


class Groups(models.Model):

    #__Groups_FIELDS__
    id = models.IntegerField(null=True, blank=True)
    name = models.TextField(max_length=255, null=True, blank=True)

    #__Groups_FIELDS__END

    class Meta:
        verbose_name        = _("Groups")
        verbose_name_plural = _("Groups")


class Projects(models.Model):

    #__Projects_FIELDS__
    id = models.IntegerField(null=True, blank=True)
    name = models.TextField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)
    start_time = models.DateTimeField(blank=True, null=True, default=timezone.now)
    end_time = models.DateTimeField(blank=True, null=True, default=timezone.now)
    status = models.TextField(max_length=255, null=True, blank=True)

    #__Projects_FIELDS__END

    class Meta:
        verbose_name        = _("Projects")
        verbose_name_plural = _("Projects")


class Project_Assignment(models.Model):

    #__Project_Assignment_FIELDS__
    id = models.IntegerField(null=True, blank=True)
    user_id = models.ForeignKey(user, on_delete=models.CASCADE)
    project_id = models.ForeignKey(projects, on_delete=models.CASCADE)

    #__Project_Assignment_FIELDS__END

    class Meta:
        verbose_name        = _("Project_Assignment")
        verbose_name_plural = _("Project_Assignment")



#__MODELS__END
