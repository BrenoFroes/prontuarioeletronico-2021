from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserCreationForm, UserChangeForm
from .models import User


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('nome', 'admin')
    list_filter = ('admin', 'staff', 'medico', 'recepcionista')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': (['cpf', 'nome', 'crm'])}),
        ('Permissions', {'fields': ('admin', 'staff', 'medico', 'recepcionista', 'active')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'cpf', 'nome', 'crm')
        }),
    )
    search_fields = ('email', 'nome', 'cpf',)
    ordering = ('nome',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)

#  Remove Group Model from admin. We're not using it.
admin.site.unregister(Group)
