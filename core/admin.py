from django.contrib import admin
from .models import ContactModal
# Register your models here.
@admin.register(ContactModal)
class AdminContact(admin.ModelAdmin):
    list_display = ['name','email','sub','msg']
