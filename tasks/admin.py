from django.contrib import admin
from tasks.models import Task, Status, Level


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'level', 'status', 'user', )
    list_filter = ('status', 'user', )
    fieldsets = (
        ("General", {
            'fields': ('name', 'status', 'level', 'user', )
        }),
    )


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', )
#    list_filter = ('name', )
    fieldsets = (
        ("General", {
            'fields': ('name', 'order', )
        }),
    )


@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', )
#    list_filter = ('name', )
    fieldsets = (
        ("General", {
            'fields': ('name', 'order', )
        }),
    )
