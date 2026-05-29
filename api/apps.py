from django.apps import AppConfig


class ApiConfig(AppConfig):
    def ready(self):
        from django.contrib.auth import get_user_model
        from django.db.utils import OperationalError
        User = get_user_model()
        try:
            from .models import UserProfile
            # Ensure admin user exists and has admin role
            admin_user = User.objects.filter(username='admin').first()
            if not admin_user:
                admin_user = User.objects.create_user(username='admin', email='admin@gmail.com', password='admin123')
                UserProfile.objects.create(user=admin_user, role='admin')
            else:
                # Update email and password if they differ
                if admin_user.email != 'admin@gmail.com':
                    admin_user.email = 'admin@gmail.com'
                admin_user.set_password('admin123')
                admin_user.save()
                UserProfile.objects.update_or_create(user=admin_user, defaults={'role': 'admin'})
            # Ensure bfp user exists and has bfp role
            bfp_user = User.objects.filter(username='bfp').first()
            if not bfp_user:
                bfp_user = User.objects.create_user(username='bfp', email='bfp@gmail.com', password='bfp123')
                UserProfile.objects.create(user=bfp_user, role='bfp')
            else:
                if bfp_user.email != 'bfp@gmail.com':
                    bfp_user.email = 'bfp@gmail.com'
                bfp_user.set_password('bfp123')
                bfp_user.save()
                UserProfile.objects.update_or_create(user=bfp_user, defaults={'role': 'bfp'})
        except OperationalError:
            # Database might not be ready yet (e.g., during migrations)
            pass
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
