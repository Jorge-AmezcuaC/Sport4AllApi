from django.apps import AppConfig


class Sport4AllConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sport4all'

    def ready(self):
        import sport4all.signals
