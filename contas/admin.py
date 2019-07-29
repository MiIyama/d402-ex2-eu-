from django.contrib import admin
from contas import models

# Register your models here.
admin.site.register(models.Pessoa)
admin.site.register(models.Conta)
