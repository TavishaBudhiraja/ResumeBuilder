from django.urls import path
from . import views


urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("signup/", views.signup, name="signup"),
    path("create-resume/", views.home, name="home"),
    path("resume-form/", views.home, name="resume_form"),
    path("preview/<int:resume_id>/", views.resume_preview, name="resume_preview"),
]