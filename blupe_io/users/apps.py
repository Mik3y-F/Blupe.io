from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "blupe_io.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import blupe_io.users.signals  # noqa F401
        except ImportError:
            pass
