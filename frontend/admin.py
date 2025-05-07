from django.contrib import admin
from .models import InvitationCode
# Register your models here.
@admin.register(InvitationCode)
class InvitationCodeAdmin(admin.ModelAdmin):
    list_display = ('code', 'description', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('code', 'description')
    ordering = ('code',)