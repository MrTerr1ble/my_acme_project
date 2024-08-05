from django.contrib import admin
from .models import Birthday


class BirthdayAdmin(admin.ModelAdmin):
    list_display = (
        'last_name',
        'first_name',
        'birthday'
    )

    list_editable = (
        'first_name',
        'birthday'
    )


admin.site.register(Birthday, BirthdayAdmin)
