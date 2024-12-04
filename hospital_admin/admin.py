from django.contrib import admin
from hospital_admin.models import HospitalAdmin, AdminManagement,Article

@admin.register(HospitalAdmin)
class HospitalAdminAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'position', 'email', 'contact_number')
    search_fields = ('full_name', 'email', 'position')

@admin.register(AdminManagement)
class AdminManagementAdmin(admin.ModelAdmin):
    list_display = ('service', 'doctor', 'patient', 'appointment', 'billing')
    search_fields = ('service__name', 'doctor__full_name', 'patient__full_name', 'appointment__appointment_id')
    list_filter = ('service', 'doctor', 'patient')




admin.site.register(Article)