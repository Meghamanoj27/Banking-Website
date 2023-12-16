from django.contrib import admin
from .models import District, Branch, Account, Material

admin.site.register(District)
admin.site.register(Branch)
admin.site.register(Material)


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'dob', 'age', 'gender', 'phone_number', 'mail_id', 'address', 'district', 'branch', 'account_type',)
    list_filter = ('district', 'branch', 'account_type', 'materials_provide',)
    search_fields = ('name', 'phone_number', 'mail_id',)
