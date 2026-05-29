from django.apps import AppConfig


class ApiConfig(AppConfig):
    def ready(self):
        from django.contrib.auth import get_user_model
        from django.db.utils import OperationalError
        User = get_user_model()
        try:
            if not User.objects.filter(username='admin').exists():
                User.objects.create_user(username='admin', password='admin123')
            if not User.objects.filter(username='bfp').exists():
                User.objects.create_user(username='bfp', password='bfp123')
        except OperationalError:
            # Database might not be ready yet (e.g., during migrations)
            pass
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
