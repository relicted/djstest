from django.apps import AppConfig


class StoreConfig(AppConfig):
    name = 'app.store'

    def ready(self):
        # import signal handlers
        import app.store.signals