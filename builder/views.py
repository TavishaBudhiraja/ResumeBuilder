from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views.decorators.cache import never_cache

from .models import Resume


def join_multiple_inputs(values):
    return "\n".join(
        value.strip()
        for value in values
        if value.strip()
    )


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("dashboard")
    else:
        form = UserCreationForm()

    return render(request, "registration/signup.html", {"form": form})

@never_cache
@login_required
def dashboard(request):
    total_resumes = Resume.objects.filter(user=request.user).count()
    latest_resume = Resume.objects.filter(user=request.user).order_by("-id").first()

    context = {
        "total_resumes": total_resumes,
        "latest_resume": latest_resume,
    }

    return render(request, "builder/dashboard.html", context)

@never_cache
@login_required
def home(request):
    if request.method == "POST":
        resume = Resume.objects.create(
            user=request.user,
            template_choice=request.POST.get("template_choice", "modern_sidebar"),
            color_theme=request.POST.get("color_theme", "navy_rose"),
            full_name=request.POST.get("full_name", "").strip(),
            email=request.POST.get("email", "").strip(),
            phone=request.POST.get("phone", "").strip(),
            address=request.POST.get("address", "").strip(),
            linkedin=request.POST.get("linkedin", "").strip(),
            github=request.POST.get("github", "").strip(),
            career_objective=request.POST.get("career_objective", "").strip(),
            skills=request.POST.get("skills", "").strip(),
            education=join_multiple_inputs(request.POST.getlist("education")),
            experience=join_multiple_inputs(request.POST.getlist("experience")),
            projects=join_multiple_inputs(request.POST.getlist("projects")),
            certifications=join_multiple_inputs(request.POST.getlist("certifications")),
        )

        return redirect("resume_preview", resume_id=resume.id)

    context = {
        "template_choices": Resume.TEMPLATE_CHOICES,
        "color_choices": Resume.COLOR_CHOICES,
    }

    return render(request, "builder/home.html", context)

@never_cache
@login_required
def resume_preview(request, resume_id):
    resume = get_object_or_404(
        Resume,
        id=resume_id,
        user=request.user
    )

    skills_list = [
        skill.strip()
        for skill in (resume.skills or "").split(",")
        if skill.strip()
    ]

    context = {
        "resume": resume,
        "skills_list": skills_list,
    }

    return render(request, "builder/resume_preview.html", context)