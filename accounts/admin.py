from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import User
from django.contrib.auth.forms import UserChangeForm


class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User


@admin.register(User)
class MyUserAdmin(UserAdmin):
    form = MyUserChangeForm
    list_display = ('username', 'first_name', 'last_name', 'auctioneer', 'is_active', 'is_staff', 'is_superuser', )

    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('auctioneer', 'note', 'birth_date', )}),
    )
