# Generated by Django 5.1.7 on 2025-06-18 21:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("health_data", "0002_healthtip_alter_appointment_options_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="MotivationVideo",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=200, verbose_name="Başlık")),
                ("description", models.TextField(max_length=500, verbose_name="Açıklama")),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("confidence", "Özgüven"),
                            ("focus", "Odaklanma"),
                            ("productivity", "Üretkenlik"),
                            ("morning_routine", "Sabah Rutini"),
                            ("other", "Diğer"),
                        ],
                        max_length=50,
                        verbose_name="Kategori",
                    ),
                ),
                (
                    "video_source",
                    models.CharField(
                        choices=[("youtube", "YouTube"), ("vimeo", "Vimeo"), ("local", "Yerel Video")],
                        max_length=20,
                        verbose_name="Video Kaynağı",
                    ),
                ),
                (
                    "video_url",
                    models.URLField(
                        help_text="YouTube/Vimeo linki veya yerel video dosyası yolu", verbose_name="Video URL"
                    ),
                ),
                (
                    "duration",
                    models.PositiveIntegerField(
                        help_text="Video süresi (saniye cinsinden)", verbose_name="Süre (saniye)"
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="Eklenme Tarihi")),
                ("is_active", models.BooleanField(default=True, verbose_name="Aktif")),
            ],
            options={
                "verbose_name": "Motivasyon Videosu",
                "verbose_name_plural": "Motivasyon Videoları",
                "ordering": ["-created_at"],
            },
        ),
    ]
