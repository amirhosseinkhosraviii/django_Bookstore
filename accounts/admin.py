from django.contrib import admin
from django.contrib.auth.admin import UserAdmin  # forms
from .forms import CustomUserChangeForm, CustomUserCreationForm  # forms
from .models import CustomUser  # model


class CustomUserAdmin(UserAdmin):

    add_form = CustomUserCreationForm

    form = CustomUserChangeForm

    models = CustomUser

    list_display = ['username', 'email', 'age', 'is_staff']

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('age',)}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('age',)}),

    )


admin.site.register(CustomUser, CustomUserAdmin)

