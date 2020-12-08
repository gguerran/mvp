from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin

from mvp.accounts.models import User, Advertiser

admin.site.unregister(Group)


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = [
        'email', 'name', 'is_superuser'
    ]
    search_fields = ['name', 'email']
    ordering = ['created_at']

    fieldsets = [
        ['Personal info', {'fields': ['name', 'email']}],
        ['Permissions', {'fields': ['is_superuser']}],
    ]
    add_fieldsets = [
        ['Informações pessoais', {
            'fields': ['name', 'email', 'password1', 'password2']
            }
        ],
        ['Permissões', {'fields': ['is_superuser',]}],
    ]


@admin.register(Advertiser)
class AdvertiserAdmin(UserAdmin):
    list_display = [
        'name', 'email', 'phone'
    ]
    list_filter = []
    search_fields = ['name', 'email']
    ordering = ['created_at']

    fieldsets = [
        ['Personal info', {'fields': ['name', 'email', 'phone']}],
    ]
    add_fieldsets = [
        ['Informações pessoais', {
            'fields': ['name', 'email', 'phone', 'password1', 'password2']
            }
        ],
    ]