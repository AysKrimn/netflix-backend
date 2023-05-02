from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import NewUser

class CustomUserAdmin(UserAdmin):
    model = NewUser
    list_display = ('username',)
    fieldsets = UserAdmin.fieldsets + (
        ('Profil Alanı', {'fields': ('avatar',)}),
    )

admin.site.register(NewUser, CustomUserAdmin)
# Register your models here.
