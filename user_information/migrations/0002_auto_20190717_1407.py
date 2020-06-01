# Generated by Django 2.2.2 on 2019-07-17 08:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_information', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinformation',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_information', to=settings.AUTH_USER_MODEL),
        ),
    ]
