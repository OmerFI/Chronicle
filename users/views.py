# Create your views here.

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import (
    PasswordChangeView,
    PasswordResetCompleteView,
    PasswordResetConfirmView,
    PasswordResetDoneView,
    PasswordResetView,
)
from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from health_data.models import Exercise, Medication, Sleep, VitalSigns

from .forms import CustomUserChangeForm, CustomUserCreationForm


def login_view(request):
    """Kullanıcı girişi görünümü"""
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("core:dashboard")
        else:
            messages.error(request, "Geçersiz e-posta veya şifre.")
    return render(request, "users/login.html")


@login_required
def logout_view(request):
    """Kullanıcı çıkışı görünümü"""
    logout(request)
    return redirect("core:home")


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Hesabınız başarıyla oluşturuldu!")
            return redirect("core:dashboard")
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = CustomUserCreationForm()
    return render(request, "users/register.html", {"form": form})


@login_required
def profile(request):
    """Kullanıcı profili görünümü"""
    return render(request, "users/profile.html")


@login_required
def profile_edit(request):
    """Kullanıcı profili düzenleme görünümü"""
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profiliniz başarıyla güncellendi.")
            return redirect("users:profile")
    else:
        form = CustomUserChangeForm(instance=request.user)
    return render(request, "users/profile_edit.html", {"form": form})


class CustomPasswordChangeView(PasswordChangeView):
    template_name = "users/password_change.html"
    success_url = reverse_lazy("users:profile")


class CustomPasswordResetView(PasswordResetView):
    """Şifre sıfırlama görünümü"""

    template_name = "users/password_reset.html"
    email_template_name = "users/password_reset_email.html"
    subject_template_name = "users/password_reset_subject.txt"
    success_url = reverse_lazy("users:password_reset_done")


class CustomPasswordResetDoneView(PasswordResetDoneView):
    """Şifre sıfırlama e-postası gönderildi görünümü"""

    template_name = "users/password_reset_done.html"


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    """Şifre sıfırlama onay görünümü"""

    template_name = "users/password_reset_confirm.html"
    success_url = reverse_lazy("users:password_reset_complete")


class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    """Şifre sıfırlama tamamlandı görünümü"""

    template_name = "users/password_reset_complete.html"


@login_required
def dashboard(request):
    """Ana dashboard görünümü"""
    # Son 7 günlük vital bulgular
    vitals = VitalSigns.objects.filter(user=request.user).order_by("-date")[:7]

    # Aktif ilaçlar
    medications = Medication.objects.filter(user=request.user, is_active=True)

    # Son 7 günlük egzersizler
    exercises = Exercise.objects.filter(user=request.user).order_by("-date")[:7]

    # Son 7 günlük uyku kayıtları
    sleeps = Sleep.objects.filter(user=request.user).order_by("-date")[:7]

    context = {
        "vitals": vitals,
        "medications": medications,
        "exercises": exercises,
        "sleeps": sleeps,
    }
    return render(request, "users/dashboard.html", context)
