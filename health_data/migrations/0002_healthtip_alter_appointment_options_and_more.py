# Generated by Django 5.1.7 on 2025-06-11 16:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("health_data", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="HealthTip",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=200, verbose_name="Başlık")),
                ("content", models.TextField(verbose_name="İçerik")),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("general", "Genel"),
                            ("exercise", "Egzersiz"),
                            ("nutrition", "Beslenme"),
                            ("sleep", "Uyku"),
                            ("medication", "İlaç Kullanımı"),
                            ("mental", "Mental Sağlık"),
                        ],
                        default="general",
                        max_length=50,
                        verbose_name="Kategori",
                    ),
                ),
                ("is_active", models.BooleanField(default=True, verbose_name="Aktif")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name": "Sağlık İpucu",
                "verbose_name_plural": "Sağlık İpuçları",
                "ordering": ["-created_at"],
            },
        ),
        migrations.AlterModelOptions(
            name="appointment",
            options={"ordering": ["date", "time"], "verbose_name": "Randevu", "verbose_name_plural": "Randevular"},
        ),
        migrations.AddField(
            model_name="appointment",
            name="department",
            field=models.CharField(default="Genel", max_length=100, verbose_name="Bölüm"),
        ),
        migrations.AddField(
            model_name="appointment",
            name="time",
            field=models.TimeField(default="09:00", verbose_name="Saat"),
        ),
        migrations.AlterField(
            model_name="appointment",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="appointment",
            name="date",
            field=models.DateField(verbose_name="Tarih"),
        ),
        migrations.AlterField(
            model_name="appointment",
            name="doctor",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="doctor_appointments",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="appointment",
            name="notes",
            field=models.TextField(blank=True, null=True, verbose_name="Notlar"),
        ),
        migrations.AlterField(
            model_name="appointment",
            name="patient",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="patient_appointments",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="appointment",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.CreateModel(
            name="DailyActivity",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("date", models.DateField(auto_now_add=True)),
                ("steps", models.PositiveIntegerField(default=0, verbose_name="Adım Sayısı")),
                (
                    "water_intake",
                    models.DecimalField(decimal_places=1, default=0, max_digits=4, verbose_name="Su Tüketimi (L)"),
                ),
                ("notes", models.TextField(blank=True, null=True, verbose_name="Notlar")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="daily_activities",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Günlük Aktivite",
                "verbose_name_plural": "Günlük Aktiviteler",
                "ordering": ["-date"],
                "unique_together": {("user", "date")},
            },
        ),
    ]
