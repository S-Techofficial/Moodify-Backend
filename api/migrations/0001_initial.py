from django.db import migrations
from api.user.models import CustomUser
from dotenv import load_dotenv
import os


class Migration(migrations.Migration):
    def seed_data(apps, schema_editor):
        user = CustomUser(name=os.getenv("ADMIN_NAME"), email=os.getenv("ADMIN_EMAIL"),
                          is_staff=True, is_superuser=True, phone=os.getenv("ADMIN_PHONENO"), gender=os.getenv("ADMIN_GENDER"))
        user.set_password(os.getenv("ADMIN_PASSWORD"))
        user.save()

    dependencies = [

    ]

    operations = [
        migrations.RunPython(seed_data),
    ]
