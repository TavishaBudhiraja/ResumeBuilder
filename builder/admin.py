from django.contrib import admin
from .models import Resume


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = (
        "full_name",
        "email",
        "phone",
        "template_choice",
        "color_theme",
        "created_at",
    )

    search_fields = (
        "full_name",
        "email",
        "phone",
    )

    list_filter = (
        "template_choice",
        "color_theme",
        "created_at",
    )