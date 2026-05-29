from django.apps import AppConfig


class ApiConfig(AppConfig):
    def ready(self):
        from django.contrib.auth import get_user_model
        from django.db.utils import OperationalError
        User = get_user_model()
        try:
            # Create admin user
            if not User.objects.filter(username='admin').exists():
                admin_user = User.objects.create_user(
                    username='admin',
                    email='admin@example.com',
                    password='admin123'
                )
                from .models import UserProfile
                UserProfile.objects.create(user=admin_user, role='admin')
            # Create bfp user
            if not User.objects.filter(username='bfp').exists():
                bfp_user = User.objects.create_user(
                    username='bfp',
                    email='bfp@example.com',
                    password='bfp123'
                )
                from .models import UserProfile
                UserProfile.objects.create(user=bfp_user, role='bfp')
        except OperationalError:
            # Database might not be ready yet (e.g., during migrations)
            pass
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
