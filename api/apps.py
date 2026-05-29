from django.apps import AppConfig


class ApiConfig(AppConfig):
    def ready(self):
        from django.contrib.auth import get_user_model
        from django.db.utils import OperationalError
        User = get_user_model()
        try:
            from .models import UserProfile
            # Ensure admin user exists and has admin role
            admin_user, created = User.objects.get_or_create(
                username='admin',
                defaults={'email': 'admin@example.com', 'password': 'admin123'}
            )
            if created:
                UserProfile.objects.create(user=admin_user, role='admin')
            else:
                UserProfile.objects.update_or_create(user=admin_user, defaults={'role': 'admin'})
            # Ensure bfp user exists and has bfp role
            bfp_user, created_bfp = User.objects.get_or_create(
                username='bfp',
                defaults={'email': 'bfp@example.com', 'password': 'bfp123'}
            )
            if created_bfp:
                UserProfile.objects.create(user=bfp_user, role='bfp')
            else:
                UserProfile.objects.update_or_create(user=bfp_user, defaults={'role': 'bfp'})
        except OperationalError:
            # Database might not be ready yet (e.g., during migrations)
            pass
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
