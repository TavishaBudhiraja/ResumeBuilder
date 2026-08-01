from django.db import models
from django.contrib.auth.models import User


class Resume(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    TEMPLATE_CHOICES = [
        ("modern_sidebar", "Modern Sidebar"),
        ("classic_single", "Classic Single Column"),
        ("creative_header", "Creative Header"),
        ("executive_dark", "Executive Dark"),
        ("minimalist_clean", "Minimalist Clean"),
        ("tech_grid", "Tech Grid"),
        ("elegant_left", "Elegant Left Panel"),
        ("academic_formal", "Academic Formal"),
        ("compact_ats", "Compact ATS Friendly"),
        ("gradient_portfolio", "Gradient Portfolio"),
    ]

    COLOR_CHOICES = [
        ("navy_rose", "Navy Rose"),
        ("blue_tech", "Blue Tech"),
        ("black_gold", "Black Gold"),
        ("emerald_forest", "Emerald Forest"),
        ("teal_cyan", "Teal Cyan"),
        ("maroon_wine", "Maroon Wine"),
        ("graphite_red", "Graphite Red"),
        ("indigo_sky", "Indigo Sky"),
        ("orange_sunset", "Orange Sunset"),
        ("slate_lime", "Slate Lime"),
        ("royal_purple", "Royal Purple"),
        ("brown_copper", "Brown Copper"),
    ]

    template_choice = models.CharField(
        max_length=40,
        choices=TEMPLATE_CHOICES,
        default="modern_sidebar"
    )

    color_theme = models.CharField(
        max_length=40,
        choices=COLOR_CHOICES,
        default="navy_rose"
    )

    full_name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=250, blank=True, null=True)

    linkedin = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)

    career_objective = models.TextField()
    skills = models.TextField()

    education = models.TextField()
    experience = models.TextField(blank=True, null=True)
    projects = models.TextField(blank=True, null=True)
    certifications = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name