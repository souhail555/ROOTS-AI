from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Car, Project, User


class CustomUserAdmin(UserAdmin):
    list_display = (
        'id',
        'username',
        'email',
        'role',
        'is_active',
        'is_staff',
        'is_superuser',
        'last_login',
    )
    list_filter = ('role', 'is_active', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role',)}),
    )


@admin.register(User)
class RegisteredCustomUserAdmin(CustomUserAdmin):
    pass


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'owner', 'cars_total')
    list_filter = ('owner__role',)
    search_fields = ('name', 'description', 'owner__username')
    autocomplete_fields = ('owner',)

    @admin.display(description='Cars')
    def cars_total(self, obj):
        return obj.cars.count()


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'car_type', 'owner', 'project')
    list_filter = ('car_type', 'owner__role')
    search_fields = ('name', 'car_type', 'owner__username', 'project__name')
    autocomplete_fields = ('owner', 'project')
