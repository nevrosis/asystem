from django.db import models
from django.db.models import CharField, TextField, BooleanField, IntegerField
from accounts.models import User


class Status(models.Model):
    name = CharField(max_length=255, verbose_name='Name')
    order = IntegerField(verbose_name='Order', default=0)
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True,)
    modified_date = models.DateTimeField(auto_now=True, blank=True, null=True,)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = "Status",
        verbose_name_plural = "Status"


class Level(models.Model):
    name = CharField(max_length=255, verbose_name='Name')
    order = IntegerField(verbose_name='Order', default=0)
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True,)
    modified_date = models.DateTimeField(auto_now=True, blank=True, null=True,)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Task(models.Model):
    name = CharField(max_length=255, verbose_name='Name')
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True,)
    modified_date = models.DateTimeField(auto_now=True, blank=True, null=True,)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, verbose_name='Status', blank=True, null=True,)
    level = models.ForeignKey(Level, on_delete=models.CASCADE, verbose_name='Status', blank=True, null=True,)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('status',)
