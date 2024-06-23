#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from vosk import SetLogLevel


def main():
    """Run administrative tasks."""


    # Voskのログレベルを設定
    SetLogLevel(-1)

    # TensorFlowのログレベルを設定
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
    
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main.settings")


    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
