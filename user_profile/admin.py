from django.contrib import admin
from user_profile.models import Profile
# Register your models here.


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)
    fieldsets = (
        (None, {
            'fields': ('user',)
        }),
    )

admin.site.register(Profile)

