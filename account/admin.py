from django.contrib import admin
from account.models import InvitationCode

class InvitationCodeAdmin(admin.ModelAdmin):
	list_display = ['code']

# Register your models here.
admin.site.register(InvitationCode, InvitationCodeAdmin)