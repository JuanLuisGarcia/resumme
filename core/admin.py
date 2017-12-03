from django.contrib import admin
from core.models import ProviderProfile, Course, Provider, Status, CourseStatus, Bio

class CourseStatusAdmin(admin.ModelAdmin):
    list_display = ('profile', 'course', 'status')
    list_filter = ('status', 'course')


class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'provider', 'url')
    list_filter = ('provider',)


class ProviderProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'username_provider', 'provider')
    list_filter = ('provider',)

class BioAdmin(admin.ModelAdmin):
    list_display = ('user', 'birth_date')


admin.site.register(ProviderProfile, ProviderProfileAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Provider)
admin.site.register(Status)
admin.site.register(Bio, BioAdmin)
admin.site.register(CourseStatus, CourseStatusAdmin)

