from django.db import migrations
from api.user.models import CustomUser


class Migration(migrations.Migration):
    def seed_data(apps, schema_editor):
        user = CustomUser(name="sumit", email="sumitln2000@gmail.com",
                          is_staff=True, is_superuser=True, phone="987654321", gender="Male")
        user.set_password("admin123")
        user.save()

    dependencies = [

    ]

    operations = [
        migrations.RunPython(seed_data),
    ]
