from .models import Profile, Branch
from django.contrib import admin


class ProfileAdmin(admin.ModelAdmin):
    list_display = "pk", "user", "email", "country"


class BranchAdmin(admin.ModelAdmin):
    list_display = "pk", "name"


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Branch, BranchAdmin)