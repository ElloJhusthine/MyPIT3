from django.contrib.auth.models import User

def create_superuser():
    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser("admin", "admin@gmail.com", "Jhusthine@123")
        print("Superuser created")
    else:
        print("Superuser already exists")
