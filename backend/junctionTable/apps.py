from django.apps import AppConfig


class JunctiontableConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "junctionTable"

    def ready(self):
        import junctionTable.signals  # your_app はシグナルが定義されているアプリの名前を指定してください