"""Build settings used in Dockerfile."""

from .base import *  # noqa: F403

SECRET_KEY = "dummy"  # noqa: S105

DEBUG = False

ALLOWED_HOSTS = []
