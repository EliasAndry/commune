# Generated by Django 4.1.3 on 2023-01-14 13:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('commune_app', '0002_alter_user_groups_alter_user_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='commune',
            name='founder',
            field=models.ForeignKey(default=346, on_delete=django.db.models.deletion.CASCADE,
                                    to=settings.AUTH_USER_MODEL),
        ),
    ]
